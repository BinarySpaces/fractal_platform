from src.schemas.requests.base_params import BaseParams


class JuliaParams(BaseParams):
    c_real: float = -0.4
    c_imag: float = 0.6
    scheme: str
    power: int = 2
