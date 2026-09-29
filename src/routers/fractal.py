from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models import BaseParams
from src.services import (
    create_one,
    delete_one,
    generate_random_fractal,
    get_one,
    list_fractals,
)

router = APIRouter(prefix='/fractal', tags=['fractal'])


def _serialize(fractal) -> dict:
    return {
        'id': fractal.id,
        'fractal_name': fractal.fractal_name,
        'scheme': fractal.scheme,
        'image_url': fractal.image_url,
        'created_at': fractal.created_at.isoformat(),
    }


@router.post('/generate')
async def create_fractal(
    params: BaseParams,
    session: AsyncSession = Depends(get_session),
) -> dict:
    # 1. генерация PNG
    gen = await generate_random_fractal(params)

    # 2. сохранение в БД
    fractal = await create_one(
        user_id=1,   # ← заглушка, потом из JWT / Depends(get_current_user_id),
        fractal_name=gen['fractal_name'],
        scheme=gen['scheme'],
        image_url=gen['image_url'],
        session=session,
    )

    return _serialize(fractal)


@router.get('/my')
async def my_fractals(
    session: AsyncSession = Depends(get_session),
) -> list[dict]:
    fractals = await list_fractals(user_id=1, session=session)

    return [_serialize(f) for f in fractals]


@router.get('/{fractal_id}')
async def get_fractal(
    fractal_id: int,
    session: AsyncSession = Depends(get_session),
) -> dict:
    fractal = await get_one(
        fractal_id=fractal_id,
        user_id=1,
        session=session,
    )

    if fractal is None:
        raise HTTPException(404, 'Fractal not found')
    return _serialize(fractal)


@router.delete('/{fractal_id}')
async def delete_fractal(
    fractal_id: int,
    session: AsyncSession = Depends(get_session),
) -> dict:
    deleted = await delete_one(
        fractal_id=fractal_id,
        user_id=1,
        session=session,
    )

    if not deleted:
        raise HTTPException(404, 'Fractal not found')
    return {'status': 'deleted', 'id': fractal_id}
