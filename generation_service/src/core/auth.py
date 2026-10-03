from fastapi import Header, HTTPException


async def get_current_user_id(authorization: str = Header(default='me')) -> int:
    print(f'[auth] получен заголовок: {authorization!r}')
    if not authorization:
        raise HTTPException(status_code=401, detail='Not authenticated')
    return 1  # Заглушка
