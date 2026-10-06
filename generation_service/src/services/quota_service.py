from datetime import datetime, timezone

from fastapi import Depends, HTTPException, status

from src.core import settings
from src.core.auth import get_current_user
from src.db.redis_client import redis_client


async def check_quota(user: dict = Depends(get_current_user)) -> None:
    user_id = user['user_id']
    is_premium = user['is_premium']

    limit = (
        settings.premium_daily_limit
        if is_premium
        else settings.free_daily_limit
    )

    key = f'quota:{user_id}:{datetime.now(timezone.utc).date().isoformat()}'

    count = await redis_client.incr(key)

    if count == 1:
        await redis_client.expire(key, 86400)

    if count > limit:
        raise HTTPException(
            status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f'Daily limit exceeded ({limit} per day)',
        )
