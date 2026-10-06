from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from src.core.config import settings


async def get_current_user_id(
        token: str = Depends(OAuth2PasswordBearer(tokenUrl='/auth/login'))
    ) -> int:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or expired token',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    user_id = payload.get('user_id')
    if not isinstance(user_id, int):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='user_id not found in token',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return user_id
