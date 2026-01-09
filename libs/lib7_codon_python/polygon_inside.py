from libs.types import PointType, PolygonType, ResultType

from .calc_insides import calc_insides


def check_points_in_polygons(
    points: list[PointType], polygons: list[PolygonType]
) -> list[ResultType]:
    return calc_insides(points, polygons)
