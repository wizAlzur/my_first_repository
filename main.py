import math


def circle_sq(r: int | float) -> int | float:
    sq = math.pi * math.pow(r, 2)
    return sq


def triangle_sq(o: int | float, h: int | float) -> int | float:
    return 0.5 * o * h


print(circle_sq(1))
print(triangle_sq(5, 2))
