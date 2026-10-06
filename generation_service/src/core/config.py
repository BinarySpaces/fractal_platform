from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    database_url: str
    redis_url: str
    free_daily_limit: int
    premium_daily_limit: int

    secret_key: str
    algorithm: str

    fractal_weights: tuple[int, ...]
    scheme_weights: tuple[int, ...]
    ifs_presets_weights: tuple[int, ...]
    l_system_presets_weights: tuple[int, ...]

    @field_validator('fractal_weights')
    @classmethod
    def validate_fractal_weights(cls, v: tuple[int, ...]) -> tuple[int, ...]:
        if sum(v) == 0:
            raise ValueError('The sum of FRACTAL_WEIGHTS can\'t be zero')
        if len(v) != 4:
            raise ValueError('FRACTAL_WEIGHTS must contain exactly 4 numbers')
        return v

    @field_validator('scheme_weights')
    @classmethod
    def validate_scheme_weights(cls, v: tuple[int, ...]) -> tuple[int, ...]:
        if sum(v) == 0:
            raise ValueError('The sum of SCHEME_WEIGHTS can\'t be zero')
        if len(v) != 4:
            raise ValueError('SCHEME_WEIGHTS must contain exactly 4 numbers')
        return v

    @field_validator('ifs_presets_weights')
    @classmethod
    def validate_ifs_presets_weights(cls, v: tuple[int, ...]) -> tuple[int, ...]:
        if sum(v) == 0:
            raise ValueError('The sum of IFS_PRESETS_WEIGHTS can\'t be zero')
        if len(v) != 10:
            raise ValueError('IFS_PRESETS_WEIGHTS must contain exactly 10 numbers')
        return v

    @field_validator('l_system_presets_weights')
    @classmethod
    def validate_l_system_presets_weights(cls, v: tuple[int, ...]) -> tuple[int, ...]:
        if sum(v) == 0:
            raise ValueError('The sum of L_SYSTEM_PRESETS_WEIGHTS can\'t be zero')
        if len(v) != 29:
            raise ValueError('L_SYSTEM_PRESETS_WEIGHTS must contain exactly 29 numbers')
        return v


settings = Settings() # type: ignore
