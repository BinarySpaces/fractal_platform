import asyncio
import math
import random

from PIL import Image, ImageDraw

from app.models.l_system_params import LSystemParams
from app.services.base_generator import BaseFractalGenerator


class LSystemGenerator(BaseFractalGenerator):
    @classmethod
    async def generate(cls, params: LSystemParams) -> str:
        return await asyncio.to_thread(cls.generate_sync, params)

    @staticmethod
    def generate_sync(params: LSystemParams) -> str:
        width = params.width
        height = params.height
        axiom = params.axiom
        rules = params.rules
        angle = params.angle
        depth = params.depth
        step = params.step

        if step is None or step <= 0:
            step = min(width, height) // 40

        current = axiom
        for _ in range(depth):
            next_str = []
            for char in current:
                next_str.append(rules.get(char, char))
            current = ''.join(next_str)

        points = []
        x, y = 0.0, 0.0
        direction = 0  # градусы
        stack = []
        points.append((x, y))

        for char in current:
            if char == 'F':
                rad = math.radians(direction)
                new_x = x + step * math.cos(rad)
                new_y = y + step * math.sin(rad)
                points.append((new_x, new_y))
                x, y = new_x, new_y
            elif char == '+':
                direction += angle
            elif char == '-':
                direction -= angle
            elif char == '[':
                stack.append((x, y, direction))
            elif char == ']':
                x, y, direction = stack.pop()

        if len(points) < 2:
            return '/static/error_l_system.png'

        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)

        range_x = max_x - min_x
        range_y = max_y - min_y

        if range_x == 0 or range_y == 0:
            return '/static/error_l_system.png'

        padding = 20
        scale = min((width - padding) / range_x, (height - padding) / range_y)
        offset_x = (width - scale * range_x) / 2 - min_x * scale
        offset_y = (height - scale * range_y) / 2 - min_y * scale

        image = Image.new('RGB', (width, height), 'black')
        draw = ImageDraw.Draw(image)

        for i in range(len(points) - 1):
            x1 = int(points[i][0] * scale + offset_x)
            y1 = int(points[i][1] * scale + offset_y)
            x2 = int(points[i + 1][0] * scale + offset_x)
            y2 = int(points[i + 1][1] * scale + offset_y)

            if ((0 <= x1 < width and 0 <= y1 < height)
                or (0 <= x2 < width and 0 <= y2 < height)):
                draw.line((x1, y1, x2, y2), fill=(255, 255, 255))

        path = f'static/l_system_{random.randint(1000, 9999)}.png'
        image.save(path)
        return f'/{path}'
