import numpy as np
from numba import njit


@njit
def is_point_at_edge_left(
    vertex1: np.ndarray, vertex2: np.ndarray, point: np.ndarray
) -> bool:
    return (vertex2[0] - vertex1[0]) * (point[1] - vertex1[1]) - (
        vertex2[1] - vertex1[1]
    ) * (point[0] - vertex1[0]) > 0


@njit
def is_point_in_polygon(point: np.ndarray, polygon: np.ndarray) -> bool:
    wn = 0
    for i in range(len(polygon)):
        vertex1 = polygon[i]
        vertex2 = polygon[(i + 1) % len(polygon)]
        is_crossing_up = vertex1[1] <= point[1] and vertex2[1] > point[1]
        is_crossing_down = vertex1[1] > point[1] and vertex2[1] <= point[1]
        if not is_crossing_up and not is_crossing_down:
            continue
        is_point_at_left = is_point_at_edge_left(vertex1, vertex2, point)
        if is_crossing_up and is_point_at_left:
            wn += 1
        elif is_crossing_down and not is_point_at_left:
            wn -= 1
    return wn != 0


@njit
def are_points_in_polygon(polygon: np.ndarray, points: np.ndarray) -> np.ndarray:
    result = np.zeros(points.shape[0], dtype=np.bool_)
    for i in range(points.shape[0]):
        result[i] = is_point_in_polygon(points[i], polygon)
    return result


def check_points_in_polygons(
    points: np.ndarray, polygons: list[np.ndarray]
) -> list[np.ndarray]:
    return [are_points_in_polygon(polygon, points) for polygon in polygons]
