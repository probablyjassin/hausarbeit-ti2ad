"""
Vereinfachte, "good-enough" 2D-Integral-Näherung ohne SciPy.
"""

from collections.abc import Callable


def integrate_2d_midpoint(
    func: Callable[[float, float], float],
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    x_steps: int = 200,
    y_steps: int = 200,
) -> float:
    """
    Approximiert das Integral über [x_min, x_max] x [y_min, y_max]
    mit der Midpoint-Rectangle-Regel.
    """
    if x_steps <= 0 or y_steps <= 0:
        raise ValueError("x_steps und y_steps müssen > 0 sein.")
    if x_max <= x_min or y_max <= y_min:
        raise ValueError("Intervallgrenzen sind ungültig.")

    dx = (x_max - x_min) / x_steps
    dy = (y_max - y_min) / y_steps

    area_sum = 0.0
    for ix in range(x_steps):
        x = x_min + (ix + 0.5) * dx
        for iy in range(y_steps):
            y = y_min + (iy + 0.5) * dy
            area_sum += func(x, y) * dx * dy

    return area_sum


# Ersatz-Hinweis:
# Dort, wo aktuell scipy.integrate.dblquad(...) aufgerufen würde,
# kann stattdessen integrate_2d_midpoint(func, x_min, x_max, y_min, y_max)
# als vereinfachte Alternative genutzt werden.
