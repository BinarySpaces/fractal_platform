from datetime import datetime, timezone

from fastapi import Depends, HTTPException

from src.core import settings
from src.core.auth import get_current_user_id
from src.db.redis_client import redis_client


async def check_quota(user_id: int = Depends(get_current_user_id)) -> None:
    is_premium = False  # заглушка

    limit = (
        settings.premium_daily_limit
        if is_premium
        else settings.free_daily_limit
    )

    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    key = f'quota:{user_id}:{today}'

    raw_count = await redis_client.get(key)
    count = int(raw_count) if raw_count else 0

    if count > limit:
        raise HTTPException(
            status_code=429,
            detail=f'Daily limit exceeded ({limit} per day)',
        )

    new_count = await redis_client.incr(key)
    if new_count == 1:
        await redis_client.expire(key, 86400)
