from typing import Callable

from .lib1_pure_python.polygon_inside import (
    check_points_in_polygons as lib1_check_points_in_polygons,
)
from .lib2_numpy.polygon_inside import (
    check_points_in_polygons as lib2_check_points_in_polygons,
)
from .lib3_shapely.polygon_inside import (
    check_points_in_polygons as lib3_check_points_in_polygons,
)
from .lib4_numba.polygon_inside import (
    check_points_in_polygons as lib4_check_points_in_polygons,
)
from .lib5_codon_numpy.polygon_inside import (
    check_points_in_polygons as lib5_check_points_in_polygons,
)
from .types import PointType, PolygonType, ResultType

# The expected function signature is:
# Args:
#   points: list of (x, y) tuples
#   polygons: list of polygons, where each polygon is a list of (x, y) tuples
# Returns:
#   A list of lists of booleans. Each inner list corresponds check results for one polygon.
#   Each boolean indicates whether the corresponding point is inside the polygon.

LIBS: dict[
    str,
    Callable[[list[PointType], list[PolygonType]], list[ResultType]],
] = {
    "lib1": lib1_check_points_in_polygons,
    "lib2": lib2_check_points_in_polygons,
    "lib3": lib3_check_points_in_polygons,
    "lib4": lib4_check_points_in_polygons,
    "lib5": lib5_check_points_in_polygons,
}
