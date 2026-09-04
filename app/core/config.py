from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    fractal_weights: tuple[int, ...] = Field(env='FRACTAL_WEIGHTS')
    scheme_weights: tuple[int, ...] = Field(env='SCHEME_WEIGHTS')
    ifs_presets_weights: tuple[int, ...] = Field(env='IFS_PRESETS_WEIGHTS')
    l_system_presets_weights: tuple[int, ...] = Field(env='L_SYSTEM_PRESETS_WEIGHTS')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    def validate_weights(self) -> None:
        if sum(self.fractal_weights) == 0:
            raise ValueError('The sum of FRACTAL_WEIGHTS can\'t be zero')
        if len(self.fractal_weights) != 4:
            raise ValueError('FRACTAL_WEIGHTS must contain exactly 4 numbers')

        if sum(self.scheme_weights) == 0:
            raise ValueError('The sum of SCHEME_WEIGHTS can\'t be zero')
        if len(self.scheme_weights) != 4:
            raise ValueError('SCHEME_WEIGHTS must contain exactly 4 numbers')

        if sum(self.ifs_presets_weights) == 0:
            raise ValueError('The sum of IFS_PRESETS_WEIGHTS can\'t be zero')
        if len(self.ifs_presets_weights) != 10:
            raise ValueError('IFS_PRESETS_WEIGHTS must contain exactly 10 numbers')

        if sum(self.l_system_presets_weights) == 0:
            raise ValueError('The sum of L_SYSTEM_PRESETS_WEIGHTS can\'t be zero')
        if len(self.l_system_presets_weights) != 29:
            raise ValueError('L_SYSTEM_PRESETS_WEIGHTS must contain exactly 29 numbers')


settings = Settings()
settings.validate_weights()
