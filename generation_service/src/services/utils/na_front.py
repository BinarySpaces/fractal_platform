# import math

# BASE_SCALE = 1.7


# def effective_max_iter(base_max_iter: int, current_scale: float) -> int:
#     """
#     Логарифмический рост max_iter при приближении.
#     """
#     if current_scale >= BASE_SCALE or current_scale <= 0:
#         return base_max_iter
#     zoom_factor = BASE_SCALE / current_scale
#     return base_max_iter + int(200 * math.log10(zoom_factor))
