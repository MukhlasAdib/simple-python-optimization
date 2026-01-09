import numpy as np


def are_points_in_polygon(polygon: np.ndarray, points: np.ndarray) -> np.ndarray:
    x, y = points[:, 0][:, None], points[:, 1][:, None]
    x1, y1 = polygon[:, 0], polygon[:, 1]
    x2, y2 = np.roll(x1, -1), np.roll(y1, -1)
    cross = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
    upward = (y1 <= y) & (y2 > y)
    downward = (y1 > y) & (y2 <= y)
    wn = np.sum(upward & (cross > 0), axis=1) - np.sum(downward & (cross < 0), axis=1)
    return wn != 0


def check_points_in_polygons(
    points: np.ndarray, polygons: list[np.ndarray]
) -> list[np.ndarray]:
    return [are_points_in_polygon(polygon, points) for polygon in polygons]
