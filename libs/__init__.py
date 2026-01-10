def load_lib1():
    from .lib1_pure_python.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib2():
    from .lib2_numpy.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib3():
    from .lib3_shapely.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib4():
    from .lib4_numba_numpy.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib5():
    from .lib5_numba_python.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib6():
    from .lib6_codon_numpy.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib7():
    from .lib7_codon_python.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_lib8():
    from .lib8_rust.polygon_inside import check_points_in_polygons

    return check_points_in_polygons


def load_vis1():
    from .vis1_python.plot_polygons import visualize

    return visualize


def load_vis2():
    from .vis2_rust.plot_polygons import visualize

    return visualize


LIBS = {
    "lib1": load_lib1,
    "lib2": load_lib2,
    "lib3": load_lib3,
    "lib4": load_lib4,
    "lib5": load_lib5,
    "lib6": load_lib6,
    "lib7": load_lib7,
    "lib8": load_lib8,
}

VIS = {
    "vis1": load_vis1,
    "vis2": load_vis2,
}
