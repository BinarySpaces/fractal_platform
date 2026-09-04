from app.services.ifs import IFSGenerator
from app.services.julia import JuliaGenerator
from app.services.l_system import LSystemGenerator
from app.services.mandelbrot import MandelbrotGenerator


class FractalFactory:

    _generators = {
        'mandelbrot': MandelbrotGenerator, # MandelbrotGenerator() creates an object
        'l_system': LSystemGenerator,
        'julia': JuliaGenerator,
        'ifs': IFSGenerator,
    }

    @classmethod
    def get_generator(cls, formula: str):
        generator = cls._generators.get(formula)
        if generator is None:
            raise ValueError(f'Unknown formula: {formula}')
        return generator
