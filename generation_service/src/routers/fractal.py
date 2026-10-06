from fastapi import APIRouter, Depends, HTTPException, status
from generation_service.src.schemas.requests import BaseParams
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.auth import get_current_user
from src.db import get_session
from src.schemas import FractalResponse
from src.services import (
    check_quota,
    create_one,
    delete_one,
    generate_random_fractal,
    get_one,
    list_fractals,
)

router = APIRouter(prefix='/fractal', tags=['fractal'])

@router.post('/generate')
async def create_fractal(
    params: BaseParams,
    _: None = Depends(check_quota),
    user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> FractalResponse:

    gen = await generate_random_fractal(params)

    fractal = await create_one(
        user_id=user['user_id'],
        fractal_name=gen['fractal_name'],
        scheme=gen['scheme'],
        image_url=gen['image_url'],
        session=session,
    )

    return FractalResponse.model_validate(fractal)


@router.get('/my')
async def my_fractals(
    session: AsyncSession = Depends(get_session),
) -> list[FractalResponse]:
    fractals = await list_fractals(user_id=1, session=session)

    return [FractalResponse.model_validate(f) for f in fractals]


@router.get('/{fractal_id}')
async def get_fractal(
    fractal_id: int,
    user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> FractalResponse:
    fractal = await get_one(
        fractal_id=fractal_id,
        user_id = user['user_id'],
        session=session,
    )

    if fractal is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Fractal not found')
    return FractalResponse.model_validate(fractal)


@router.delete('/{fractal_id}')
async def delete_fractal(
    fractal_id: int,
    session: AsyncSession = Depends(get_session),
) -> dict | None:
    deleted = await delete_one(
        fractal_id=fractal_id,
        user_id=1,
        session=session,
    )

    if not deleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Fractal not found')
    return {'status': 'deleted', 'id': fractal_id}
