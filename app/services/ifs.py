import asyncio
import random

from PIL import Image, ImageDraw

from app.models.ifs_params import IFSParams
from app.services.base_generator import BaseFractalGenerator


class IFSGenerator(BaseFractalGenerator):
    @classmethod
    async def generate(cls, params: IFSParams) -> str:
        return await asyncio.to_thread(cls.generate_sync, params)

    @staticmethod
    def generate_sync(params: IFSParams) -> str:
        width = params.width
        height = params.height
        iterations = params.iterations
        preset_transforms = params.preset_transforms

        points = []
        x, y = 0.0, 0.0

        n = len(preset_transforms)
        for _ in range(iterations):
            idx = random.randint(0, n - 1)
            a, b, c, d, e, f = preset_transforms[idx]
            new_x = a * x + b * y + e
            new_y = c * x + d * y + f
            x, y = new_x, new_y
            points.append((x, y))

        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)

        padding = 0.05
        range_x = max_x - min_x
        range_y = max_y - min_y
        min_x -= range_x * padding
        max_x += range_x * padding
        min_y -= range_y * padding
        max_y += range_y * padding

        scale_x = width / (max_x - min_x)
        scale_y = height / (max_y - min_y)

        image = Image.new('RGB', (width, height), 'black')
        draw = ImageDraw.Draw(image)

        for x, y in points:
            px = int((x - min_x) * scale_x)
            py = height - int((y - min_y) * scale_y)
            if 0 <= px < width and 0 <= py < height:
                draw.point((px, py), fill=(0, 255, 0))

        path = f'static/ifs_{random.randint(1000, 9999)}.png'
        image.save(path)
        return f'/{path}'
