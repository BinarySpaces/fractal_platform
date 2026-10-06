from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security import create_access_token, hash_password, verify_password
from src.db.models import User
from src.db.repositories import add, delete, get_by_email, get_by_id


async def register_user(email: str, password: str, session: AsyncSession) -> User | None:
    if await get_by_email(email, session) is not None:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            detail='Email already registered'
        )
    user = User(email=email, password_hash=hash_password(password))
    user = await add(user, session)
    await session.commit()
    await session.refresh(user)
    return user


async def login_user(email: str, password: str, session: AsyncSession) -> str:
    user = await get_by_email(email, session)
    if user is None or not verify_password(password, user.password_hash):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            'Invalid email or password'
        )
    return create_access_token(user.id, user.is_premium)


async def get_user(user_id: int, session: AsyncSession) -> User | None:
    return await get_by_id(user_id, session)


async def delete_user(user_id: int, session: AsyncSession) -> bool:
    user = await get_by_id(user_id, session)
    if user is None:
        return False

    await delete(user, session)
    await session.commit()
    return True
