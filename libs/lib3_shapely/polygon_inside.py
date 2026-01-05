import numpy as np
import shapely
from shapely.geometry import Polygon

from libs.types import PointType, PolygonType, ResultType


def check_points_in_polygons(
    points: list[PointType], polygons: list[PolygonType]
) -> list[ResultType]:
    polygons_shapely = np.array([Polygon(polygon) for polygon in polygons])
    points_shapely = shapely.points(points)
    is_insides = shapely.contains(polygons_shapely[:, None], points_shapely[None, :])
    return is_insides.tolist()
