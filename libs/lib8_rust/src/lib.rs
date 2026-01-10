use geo::{Coord, LineString, Point, Polygon, Contains};
use numpy::{PyArray1, PyReadonlyArray2};
use pyo3::prelude::*;
use pyo3::types::PyModule;


#[pyfunction]
fn check_points_in_polygons_rs(
    py: Python<'_>,
    points: PyReadonlyArray2<f64>,
    polygons: Vec<PyReadonlyArray2<f64>>,
) -> PyResult<Vec<Py<PyArray1<bool>>>> {
    let points_arr = points.as_array();
    let points_geo: Vec<Point<f64>> = points_arr
        .rows()
        .into_iter()
        .map(|r| Point::new(r[0], r[1]))
        .collect();

    let mut results = Vec::with_capacity(polygons.len());

    for polygon in polygons {
        let poly_arr = polygon.as_array();

        let coords: Vec<Coord<f64>> = poly_arr
            .rows()
            .into_iter()
            .map(|r| Coord { x: r[0], y: r[1] })
            .collect();

        let mut ring = coords;
        if ring.first() != ring.last() {
            ring.push(*ring.first().unwrap());
        }

        let polygon_geo = Polygon::new(LineString::from(ring), vec![]);
        let mask: Vec<bool> = points_geo
            .iter()
            .map(|p| polygon_geo.contains(p))
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
