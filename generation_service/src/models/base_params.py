from pydantic import BaseModel


class BaseParams(BaseModel):
    width: int = 1000
    height: int = 1000
    max_iter: int = 100
