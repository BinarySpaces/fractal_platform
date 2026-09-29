import asyncio
import random

import numpy as np
from PIL import Image

from src.models import JuliaParams
from src.services.utils import get_color


async def generate_julia(params: JuliaParams) -> str:
    return await asyncio.to_thread(generate_sync, params)

def generate_sync(params: JuliaParams) -> str:
    width = params.width
    height = params.height
    max_iter = params.max_iter
    scheme = params.scheme
    power = params.power

    scale = 2.0
    aspect_ratio = width / height
    x = np.linspace(-scale, scale, width)
    y = np.linspace(-scale / aspect_ratio, scale / aspect_ratio, height)

    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    img = np.zeros(Z.shape, dtype=np.int32)
    mask = np.ones(Z.shape, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask] ** power + complex(params.c_real, params.c_imag)

        new_mask = np.abs(Z) > 2
        img[new_mask & mask] = i + 1
        mask = mask & ~new_mask

    image = Image.new('RGB', (width, height))
    pixels = image.load()
    if pixels is None:
        raise RuntimeError('Failed to load pixels')

    for x in range(width):
        for y in range(height):
            i = img[y, x]
            if i == 0:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = get_color(i, max_iter, scheme)

    path = f'static/julia_{random.randint(1000, 9999)}.png'
    image.save(path)
    return f'/{path}'
