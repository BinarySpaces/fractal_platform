import asyncio
import math
import random

from generation_service.src.schemas.requests import LSystemParams
from PIL import Image, ImageDraw


async def generate_l_system(params: LSystemParams) -> str:
    return await asyncio.to_thread(generate_sync, params)

def generate_sync(params: LSystemParams) -> str:
    width = params.width
    height = params.height
    axiom = params.axiom
    rules = params.rules
    angle = params.angle
    depth = params.depth
    step = params.step

    # 1. Строка L-system
    current = axiom
    for _ in range(depth):
        current = ''.join(rules.get(c, c) for c in current)

    # 2. Обход черепашкой — получаем отрезки (x1,y1,x2,y2)
    segments = []
    x, y = 0.0, 0.0
    direction = 0
    stack = []

    for char in current:
        if char == 'F':
            rad = math.radians(direction)
            nx = x + step * math.cos(rad)
            ny = y + step * math.sin(rad)
            segments.append((x, y, nx, ny))
            x, y = nx, ny
        elif char == '+':
            direction += angle
        elif char == '-':
            direction -= angle
        elif char == '[':
            stack.append((x, y, direction))
        elif char == ']':
            x, y, direction = stack.pop()

    if not segments:
        return '/static/error_l_system.png'

    # 3. Границы
    xs = [s[i] for s in segments for i in (0, 2)]
    ys = [s[i] for s in segments for i in (1, 3)]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    pad_x = (max_x - min_x) * 0.05 or 1.0
    pad_y = (max_y - min_y) * 0.05 or 1.0
    min_x -= pad_x
    max_x += pad_x
    min_y -= pad_y
    max_y += pad_y

    # 4. Подгонка под aspect ratio
    aspect = width / height
    range_x = max_x - min_x
    range_y = max_y - min_y

    if range_x / range_y > aspect:
        new_range_y = range_x / aspect
        cy = (min_y + max_y) / 2
        min_y = cy - new_range_y / 2
        max_y = cy + new_range_y / 2
    else:
        new_range_x = range_y * aspect
        cx = (min_x + max_x) / 2
        min_x = cx - new_range_x / 2
        max_x = cx + new_range_x / 2

    # 5. Масштаб для пикселей
    scale_x = (width - 1) / (max_x - min_x)
    scale_y = (height - 1) / (max_y - min_y)

    # 6. PNG
    image = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(image)

    for (x1, y1, x2, y2) in segments:
        px1 = int((x1 - min_x) * scale_x)
        py1 = int((max_y - y1) * scale_y)   # инверсия Y
        px2 = int((x2 - min_x) * scale_x)
        py2 = int((max_y - y2) * scale_y)

        draw.line((px1, py1, px2, py2), fill='white', width=1)

    path = f'static/l_system_{random.randint(1000, 9999)}.png'
    image.save(path)
    return f'/{path}'
