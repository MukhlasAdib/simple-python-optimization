import numpy as np

from .calc_insides import calc_insides


def check_points_in_polygons(
    points: np.ndarray, polygons: list[np.ndarray]
) -> list[np.ndarray]:
    return calc_insides(polygons, points)
