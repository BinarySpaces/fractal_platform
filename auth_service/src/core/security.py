from datetime import datetime, timedelta, timezone

from jose import jwt
from pwdlib import PasswordHash

from src.core.config import settings

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(user_id: int, is_premium: bool = False) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload = {
        'user_id': user_id,
        'is_premium': is_premium,
        'exp': expire,
    }
    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )
