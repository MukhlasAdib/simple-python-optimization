from libs.types import PointType, PolygonType, ResultType


def is_point_at_edge_left(
    vertex1: PointType, vertex2: PointType, point: PointType
) -> bool:
    return (vertex2[0] - vertex1[0]) * (point[1] - vertex1[1]) - (
        vertex2[1] - vertex1[1]
    ) * (point[0] - vertex1[0]) > 0


def is_point_in_polygon(point: PointType, polygon: PolygonType) -> bool:
    wn = 0
    for i in range(len(polygon)):
        vertex1 = polygon[i]
        vertex2 = polygon[(i + 1) % len(polygon)]
        is_point_at_left = is_point_at_edge_left(vertex1, vertex2, point)
        is_crossing_up = vertex1[1] <= point[1] and vertex2[1] > point[1]
        is_crossing_down = vertex1[1] > point[1] and vertex2[1] <= point[1]
        if is_crossing_up and is_point_at_left:
            wn += 1
        elif is_crossing_down and not is_point_at_left:
            wn -= 1
    return wn != 0


def check_points_in_polygons(
    points: list[PointType], polygons: list[PolygonType]
) -> list[ResultType]:
    return [
        [is_point_in_polygon(point, polygon) for point in points]
        for polygon in polygons
    ]
