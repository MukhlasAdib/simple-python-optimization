import numpy as np
import shapely
from shapely.geometry import Polygon


def check_points_in_polygons(
    points: np.ndarray, polygons: list[np.ndarray]
) -> list[np.ndarray]:
    polygons_shapely = np.array([Polygon(polygon) for polygon in polygons])
    points_shapely = shapely.points(points)
    is_insides = shapely.contains(polygons_shapely[:, None], points_shapely[None, :])
    return list(is_insides)
