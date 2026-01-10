from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon


def visualize(
    polygons: list[np.ndarray],
    points: np.ndarray,
    results: list[np.ndarray],
    output_dir: Path,
    canvas_width: int,
    canvas_height: int,
) -> None:
    output_dir.mkdir(exist_ok=True)
    for i, (polygon, result) in enumerate(zip(polygons, results)):
        fig, ax = plt.subplots(figsize=(15, 15))
        x, y = zip(*points)
        colors = ["green" if f else "red" for f in result]
        ax.scatter(x, y, s=1, c=colors, zorder=3)
        poly_patch = Polygon(polygon, closed=True, edgecolor="blue", facecolor="none")
        ax.add_patch(poly_patch)
        ax.set_aspect("equal")
        ax.set_xlim(0, canvas_width)
        ax.set_ylim(0, canvas_height)
        plt.savefig(output_dir / f"output_{i}.png")
        plt.close(fig)
