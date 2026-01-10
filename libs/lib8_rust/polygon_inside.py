import numpy as np
from calc_insides_rs import check_points_in_polygons_rs


def check_points_in_polygons(
    points: np.ndarray, polygons: list[np.ndarray]
) -> list[np.ndarray]:
    return check_points_in_polygons_rs(points, polygons)
