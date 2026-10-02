import random

from src.core import settings
from src.models import (
    BaseParams,
    IFSParams,
    JuliaParams,
    LSystemParams,
    MandelbrotParams,
)
from src.services.fractal_factory import get_generator
from src.services.presets import IFS_PRESETS, L_SYSTEM_PRESETS


async def generate_random_fractal(params: BaseParams) -> dict:

    params_dict = params.model_dump()

    formula = random.choices(
        ['mandelbrot', 'julia', 'ifs', 'l_system'],
        weights=settings.fractal_weights,
        k=1,
    )[0]

    match formula:

        case 'mandelbrot':
            params_dict['scheme'] = random.choices(
                ('cold', 'hot', 'forest', 'clarity'),
                weights=settings.scheme_weights,
                k=1,
            )[0]
            fractal_name = 'Mandelbrot'
            scheme = params_dict['scheme']

            typed_params = MandelbrotParams(**params_dict)

        case 'julia':
            params_dict['scheme'] = random.choices(
                ('cold', 'hot', 'forest', 'clarity'),
                weights=settings.scheme_weights,
                k=1,
            )[0]
            fractal_name = 'Julia'
            scheme = params_dict['scheme']

            params_dict['c_real'] = random.uniform(-2.0, 2.0)
            params_dict['c_imag'] = random.uniform(-2.0, 2.0)
            params_dict['power'] = random.choices([2, 3, 4], weights=[3, 1, 1])[0]

            typed_params = JuliaParams(**params_dict)

        case 'ifs':
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

        case _:
            preset_name = random.choices(
                tuple(L_SYSTEM_PRESETS.keys()),
                weights=tuple(settings.l_system_presets_weights),
                k=1,
            )[0]
            fractal_name = preset_name
            scheme = None

            params_dict['preset_name'] = preset_name
            params_dict.update(L_SYSTEM_PRESETS[preset_name])

            typed_params = LSystemParams(**params_dict)

    return {
        'image_url': await get_generator(formula)(typed_params),
        'fractal_name': fractal_name,
        'scheme': scheme,
    }
