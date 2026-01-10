use numpy::{PyArray1, PyReadonlyArray2};
use pyo3::prelude::*;
use pyo3::types::PyModule;

fn is_point_at_edge_left(
    v1: [f64; 2],
    v2: [f64; 2],
    p: [f64; 2],
) -> bool {
    (v2[0] - v1[0]) * (p[1] - v1[1])
        - (v2[1] - v1[1]) * (p[0] - v1[0])
        > 0.0
}

fn is_point_in_polygon(point: [f64; 2], polygon: &[[f64; 2]]) -> bool {
    let mut wn = 0;
    let n = polygon.len();

    for i in 0..n {
        let v1 = polygon[i];
        let v2 = polygon[(i + 1) % n];

        let crossing_up = v1[1] <= point[1] && v2[1] > point[1];
        let crossing_down = v1[1] > point[1] && v2[1] <= point[1];

        if !crossing_up && !crossing_down {
            continue;
        }

        let left = is_point_at_edge_left(v1, v2, point);

        if crossing_up && left {
            wn += 1;
        } else if crossing_down && !left {
            wn -= 1;
        }
    }

    wn != 0
}

#[pyfunction]
fn check_points_in_polygons_rs(
    py: Python<'_>,
    points: PyReadonlyArray2<f64>,
    polygons: Vec<PyReadonlyArray2<f64>>,
) -> PyResult<Vec<Py<PyArray1<bool>>>> {
    let points_arr = points.as_array();

    let points_vec: Vec<[f64; 2]> = points_arr
        .rows()
        .into_iter()
        .map(|r| [r[0], r[1]])
        .collect();

    let mut results = Vec::with_capacity(polygons.len());

    for polygon in polygons {
        let poly_arr = polygon.as_array();

        let polygon_vec: Vec<[f64; 2]> = poly_arr
            .rows()
            .into_iter()
            .map(|r| [r[0], r[1]])
            .collect();

        let mask: Vec<bool> = points_vec
            .iter()
            .copied()
            .map(|p| is_point_in_polygon(p, &polygon_vec))
            .collect();

        let array = PyArray1::from_vec(py, mask);
        results.push(array.to_owned().into());
    }

    Ok(results)
}

#[pymodule]
fn calc_insides_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(check_points_in_polygons_rs))?;
    Ok(())
}
