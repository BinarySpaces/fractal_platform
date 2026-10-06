from src.schemas.requests.base_params import BaseParams


class LSystemParams(BaseParams):
    preset_name: str = ''
    axiom: str = ''
    rules: dict = {}
    angle: float = 60.0
    depth: int = 10
    step: float = 10.0
