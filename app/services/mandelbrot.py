import asyncio
import random

import numpy as np
from PIL import Image

from app.models.mandelbrot_params import MandelbrotParams
from app.services.base_generator import BaseFractalGenerator
from app.utils.color_utils import get_color


class MandelbrotGenerator(BaseFractalGenerator):
    @classmethod
    async def generate(cls, params: MandelbrotParams) -> str:
        return await asyncio.to_thread(cls.generate_sync, params)

    @staticmethod
    def generate_sync(params: MandelbrotParams) -> str:
        width = params.width
        height = params.height
        max_iter = params.max_iter
        scheme = params.scheme

        scale = 1.7
        center_x = -0.5
        center_y = 0.0

        scale_x = scale
        scale_y = scale / (width / height)

        x = np.linspace(-scale_x + center_x, scale_x + center_x, width)
        y = np.linspace(-scale_y + center_y, scale_y + center_y, height)

        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros_like(C, dtype=np.complex128)
        img = np.zeros(C.shape, dtype=np.int32)

        mask = np.ones(C.shape, dtype=bool)

        for i in range(max_iter):
            Z[mask] = Z[mask] * Z[mask] + C[mask]
            new_mask = np.abs(Z) > 2
            img[new_mask & mask] = i + 1
            mask = mask & ~new_mask

        image = Image.new('RGB', (width, height))
        pixels = image.load()

        for x in range(width):
            for y in range(height):
                i = img[y, x]
                if i == 0:
                    pixels[x, y] = (0, 0, 0)
                else:
                    pixels[x, y] = get_color(i, max_iter, scheme)

        path = f'static/mandelbrot_{random.randint(1000, 9999)}.png'
        image.save(path)
        return f'/{path}'
