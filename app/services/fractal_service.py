import random

from app.core import settings
from app.models import (
    BaseParams,
    IFSParams,
    JuliaParams,
    LSystemParams,
    MandelbrotParams,
)
from app.presets import IFS_PRESETS, L_SYSTEM_PRESETS
from app.services.fractal_factory import FractalFactory


class FractalService:

    @staticmethod
    async def generate_random_fractal(params: BaseParams):
        formula = random.choices(
            ['mandelbrot', 'julia', 'ifs', 'l_system'],
            weights=settings.fractal_weights,
            k=1
        )[0]

        params_dict = params.model_dump()

        if formula == 'mandelbrot':
            params_dict['scheme'] = random.choices(
                ('cold', 'hot', 'forest', ''),
                weights=settings.scheme_weights,
                k=1
            )[0]
            fractal_name = 'Mandelbrot'
            scheme = params_dict['scheme']

            typed_params = MandelbrotParams(**params_dict)

        elif formula == 'julia':
            params_dict['scheme'] = random.choices(
                ('cold', 'hot', 'forest', ''),
                weights=settings.scheme_weights,
                k=1
            )[0]
            fractal_name = 'Julia'
            scheme = params_dict['scheme']

            params_dict['c_real'] = random.uniform(-2.0, 2.0)
            params_dict['c_imag'] = random.uniform(-2.0, 2.0)

            typed_params = JuliaParams(**params_dict)

        elif formula == 'ifs':
            preset_name = random.choices(
                tuple(IFS_PRESETS.keys()),
                weights=settings.ifs_presets_weights,
                k=1
            )[0]
            fractal_name = preset_name
            scheme = None

            params_dict['preset_name'] = preset_name
            params_dict['preset_transforms'] = IFS_PRESETS[preset_name]
            params_dict['iterations'] = random.randint(50000, 200000)

            typed_params = IFSParams(**params_dict)

        else:
            preset_name = random.choices(
                tuple(L_SYSTEM_PRESETS.keys()),
                weights=tuple(settings.l_system_presets_weights),
                k=1
            )[0]
            fractal_name = preset_name
            scheme = None

            params_dict.update(L_SYSTEM_PRESETS[preset_name])
            params_dict['preset_name'] = preset_name

            typed_params = LSystemParams(**params_dict)

        return {
            'image_url': await FractalFactory.get_generator(
                formula
            ).generate(typed_params),
            'fractal_name': fractal_name,
            'scheme': scheme
        }
