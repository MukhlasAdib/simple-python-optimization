import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pyinstrument import Profiler

from libs import LIBS

POLYGON_DIR = Path("polygons")
OUTPUT_DIR = Path("outputs")
CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
POINT_NUMBERS = 300


def load_polygon(txt_path):
    points = []
    with open(txt_path, "r") as f:
        for line in f:
            x_str, y_str = line.strip().split()
            x = float(x_str) * CANVAS_WIDTH
            y = float(y_str) * CANVAS_HEIGHT
            points.append((x, y))
    return points


def load_all_polygons():
    polygons = []
    if not POLYGON_DIR.exists():
        return polygons
    for txt_file in POLYGON_DIR.glob("*.txt"):
        polygon = load_polygon(txt_file)
        polygons.append(polygon)
    return polygons


def visualize(polygons, points, results):
    OUTPUT_DIR.mkdir(exist_ok=True)
    for i, (polygon, result) in enumerate(zip(polygons, results)):
        fig, ax = plt.subplots(figsize=(15, 15))
        x, y = zip(*points)
        colors = ["green" if f else "red" for f in result]
        ax.scatter(x, y, s=1, c=colors, zorder=3)
        poly_patch = Polygon(polygon, closed=True, edgecolor="blue", facecolor="none")
        ax.add_patch(poly_patch)
        ax.set_aspect("equal")
        ax.set_xlim(0, CANVAS_WIDTH)
        ax.set_ylim(0, CANVAS_HEIGHT)
        plt.savefig(OUTPUT_DIR / f"output_{i}.png")
        plt.close(fig)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "lib",
        type=str,
        choices=LIBS.keys(),
        default="lib1",
        help="Library to use for point-in-polygon checking",
    )
    args = argparser.parse_args()

    polygons = load_all_polygons()
    points = [
        (i * CANVAS_WIDTH / POINT_NUMBERS, j * CANVAS_HEIGHT / POINT_NUMBERS)
        for i in range(1, POINT_NUMBERS)
        for j in range(1, POINT_NUMBERS)
    ]

    # Warmup
    LIBS[args.lib](points, polygons)

    profiler = Profiler()
    profiler.start()
    results = LIBS[args.lib](points, polygons)
    profiler.stop()
    print(profiler.output_text(unicode=True, color=True))

    visualize(polygons, points, results)


if __name__ == "__main__":
    main()
