import math


def get_color(i: int, max_iter: int, scheme: str) -> tuple:
    if max_iter > 100:
        if i == 0:
            smooth = 0.0
        else:
            smooth = math.log(i) / math.log(max_iter)
    else:
        smooth = i / max_iter

    if scheme == 'hot':
        r = int(min(1.0, smooth * 8.0) * 255)
        g = int(min(1.0, smooth * 5.5) * 255)
        b = int(min(1.0, smooth * 4.5) * 255)
        return (r, g, b)

    elif scheme == 'cold':
        r = int(min(1.0, smooth * 4.5) * 255)
        g = int(min(1.0, smooth * 5.5) * 255)
        b = int(min(1.0, smooth * 8.0) * 255)
        return (r, g, b)

    elif scheme == 'forest':
        r = int(min(1.0, smooth * 4.5) * 255)
        g = int(min(1.0, smooth * 8.0) * 255)
        b = int(min(1.0, smooth * 5.5) * 255)
        return (r, g, b)

    else:
        return (i * 5 % 255, i * 10 % 255, i * 15 % 255)
