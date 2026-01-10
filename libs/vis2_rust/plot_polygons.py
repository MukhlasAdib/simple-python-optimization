from pathlib import Path

import numpy as np
from plot_polygons_rs import visualize_rs


def visualize(
    polygons: list[np.ndarray],
    points: np.ndarray,
    results: list[np.ndarray],
    output_dir: Path,
    canvas_width: int,
    canvas_height: int,
) -> None:
    visualize_rs(
        polygons=polygons,
        points=points,
        results=results,
        output_dir=output_dir,
        canvas_width=canvas_width,
        canvas_height=canvas_height,
    )
