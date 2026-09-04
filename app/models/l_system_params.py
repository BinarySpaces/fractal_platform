from typing import Optional

from app.models.base_params import BaseParams


class LSystemParams(BaseParams):
    preset: str = 'koch_snowflake'
    axiom: str = 'F'
    rules: dict = {'F': 'F-F++F-F'}
    angle: float = 60.0
    depth: int = 4
    step: Optional[int] = None
