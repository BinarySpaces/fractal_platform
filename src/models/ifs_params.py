from src.models.base_params import BaseParams


class IFSParams(BaseParams):
    preset_name: str = ''
    iterations: int = 100000
    preset_transforms: list = []
