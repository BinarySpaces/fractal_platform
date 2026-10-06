from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Fractal
from src.db.repositories import add, delete, get_by_id, list_by_user


async def create_one(
    user_id: int,
    fractal_name: str,
    scheme: str | None,
    image_url: str,
    session: AsyncSession,
) -> Fractal:
    fractal = Fractal(
        user_id=user_id,
        fractal_name=fractal_name,
        scheme=scheme,
        image_url=image_url,
    )
    fractal = await add(fractal, session)
    await session.commit()
    await session.refresh(fractal)
    return fractal


async def get_one(
    fractal_id: int,
    user_id: int,
    session: AsyncSession,
) -> Fractal | None:
    return await get_by_id(fractal_id, user_id, session)


async def list_fractals(
    user_id: int,
    session: AsyncSession,
) -> list[Fractal]:
    return await list_by_user(user_id, session)


async def delete_one(
    fractal_id: int,
    user_id: int,
    session: AsyncSession,
) -> bool:
    fractal = await get_by_id(fractal_id, user_id, session)
    if fractal is None:
        return False

    Path(fractal.image_url.lstrip('/')).unlink(missing_ok=True)

    # s3_client.delete_object(Bucket=BUCKET, Key=fractal.image_url.lstrip('/'))

    await delete(fractal, session)
    await session.commit()
    return True
