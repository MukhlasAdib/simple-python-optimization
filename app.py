import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from pyinstrument import Profiler

from libs import LIBS, VIS

POLYGON_DIR = Path("polygons")
OUTPUT_DIR = Path("outputs")
CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
POINT_NUMBERS = 300


def load_polygon(txt_path):
    points = np.loadtxt(txt_path)
    points[:, 0] = points[:, 0] * CANVAS_WIDTH
    points[:, 1] = points[:, 1] * CANVAS_HEIGHT
    return points


def load_all_polygons():
    polygons = []
    if not POLYGON_DIR.exists():
        return polygons
    for txt_file in POLYGON_DIR.glob("*.txt"):
        polygon = load_polygon(txt_file)
        polygons.append(polygon)
    return polygons


def warmup(points, polygons):
    LIBS[args.lib](points, polygons)


def main():
    polygons = load_all_polygons()
    points = np.array(
        [
            (i * CANVAS_WIDTH / POINT_NUMBERS, j * CANVAS_HEIGHT / POINT_NUMBERS)
            for i in range(1, POINT_NUMBERS)
            for j in range(1, POINT_NUMBERS)
        ]
    )
    warmup(points, polygons)

    profiler = Profiler()
    profiler.start()
    results = LIBS[args.lib](points, polygons)
    profiler.stop()
    print(profiler.output_text(unicode=True, color=True))

    VIS[args.vis](polygons, points, results, OUTPUT_DIR, CANVAS_WIDTH, CANVAS_HEIGHT)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "lib",
        type=str,
        choices=LIBS.keys(),
        default="lib1",
        help="Library to use for point-in-polygon checking",
    )
    argparser.add_argument(
        "vis",
        type=str,
        choices=VIS.keys(),
        default="vis1",
        help="Library to use for visualization",
    )
    args = argparser.parse_args()

    main()
