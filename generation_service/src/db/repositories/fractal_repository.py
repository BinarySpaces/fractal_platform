from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import Fractal


async def add(fractal: Fractal, session: AsyncSession) -> Fractal:
    session.add(fractal)
    await session.flush()
    return fractal

async def get_by_id(
        fractal_id: int,
        user_id: int,
        session: AsyncSession
    ) -> Fractal | None:
    result = await session.execute(
        select(Fractal).where(
            Fractal.id == fractal_id,
            Fractal.user_id == user_id,
        )
    )
    return result.scalar_one_or_none()

async def list_by_user(
        user_id: int,
        session: AsyncSession,
        limit: int = 50
    ) -> list[Fractal]:
    result = await session.execute(
        select(Fractal)
        .where(Fractal.user_id == user_id)
        .order_by(desc(Fractal.created_at))
        .limit(limit)
    )
    return list(result.scalars().all())

async def delete(fractal: Fractal, session: AsyncSession) -> None:
    await session.delete(fractal)
    await session.flush()
