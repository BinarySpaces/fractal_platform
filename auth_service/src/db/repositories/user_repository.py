from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import User


async def add(user: User, session: AsyncSession) -> User:
    session.add(user)
    await session.flush()
    return user


async def get_by_id(user_id: int, session: AsyncSession) -> User | None:
    result = await session.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_by_email(email: str, session: AsyncSession) -> User | None:
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def delete(user: User, session: AsyncSession) -> None:
    await session.delete(user)
    await session.flush()
