from src.services.generators import (
    generate_ifs,
    generate_julia,
    generate_l_system,
    generate_mandelbrot,
)

_GENERATORS = {
    'ifs': generate_ifs,
    'julia': generate_julia,
    'l_system': generate_l_system,
    'mandelbrot': generate_mandelbrot  # MandelbrotGenerator() creates an object
}

def get_generator(formula: str):
    generator = _GENERATORS.get(formula)
    if generator is None:
        raise ValueError(f'Unknown formula: {formula}')
    return generator
