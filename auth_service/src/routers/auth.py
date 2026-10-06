from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.auth import get_current_user_id
from src.db.session import get_session
from src.schemas import TokenResponse, UserCreate, UserResponse
from src.services import delete_user, get_user, login_user, register_user

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(
    params: UserCreate,
    session: AsyncSession = Depends(get_session)
) -> UserResponse:
    user = await register_user(params.email, params.password, session)
    return UserResponse.model_validate(user)


@router.post('/login')
async def login(
    params: UserCreate,
    session: AsyncSession = Depends(get_session)
) -> TokenResponse:
    token = await login_user(params.email, params.password, session)
    return TokenResponse(access_token=token)


@router.get('/me')
async def me(
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session)
) -> UserResponse:
    user = await get_user(user_id, session)
    if user is None:
        raise HTTPException(status. HTTP_404_NOT_FOUND, 'User not found')
    return UserResponse.model_validate(user)


@router.delete('/{user_id}')
async def delete(
    user_id: int,
    session: AsyncSession = Depends(get_session)
) -> dict | None:
    deleted = await delete_user(user_id, session)

    if not deleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'User not found')


@router.post('/logout', status_code=status.HTTP_204_NO_CONTENT)
async def logout() -> None:
    pass
