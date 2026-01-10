use std::fs;
use std::path::PathBuf;

use numpy::{PyReadonlyArray1, PyReadonlyArray2};
use plotters::prelude::*;
use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
fn visualize_rs(
    py: Python<'_>,
    polygons: &Bound<'_, PyList>,
    points: PyReadonlyArray2<f64>,
    results: &Bound<'_, PyList>,
    output_dir: PathBuf,
    canvas_width: u32,
    canvas_height: u32,
) -> PyResult<()> {
    fs::create_dir_all(&output_dir)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(e.to_string()))?;

    let points_arr = points.as_array();
    let points: Vec<(f64, f64)> = points_arr
        .rows()
        .into_iter()
        .map(|r| (r[0], r[1]))
        .collect();

    for i in 0..polygons.len() {
        let poly_obj = polygons.get_item(i)?;
        let res_obj = results.get_item(i)?;

        let polygon: PyReadonlyArray2<f64> = poly_obj.extract()?;
        let result: PyReadonlyArray1<bool> = res_obj.extract()?;

        let polygon: Vec<(f64, f64)> = polygon
            .as_array()
            .rows()
            .into_iter()
            .map(|r| (r[0], r[1]))
            .collect();

        let result: Vec<bool> = result.as_array().iter().copied().collect();

        let filename = output_dir.join(format!("output_{}.png", i));

        let root = BitMapBackend::new(&filename, (canvas_width, canvas_height))
            .into_drawing_area();

        root.fill(&WHITE)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{:?}", e)))?;

        let mut chart = ChartBuilder::on(&root)
            .margin(10)
            .build_cartesian_2d(
                0.0..canvas_width as f64,
                0.0..canvas_height as f64,
            )
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{:?}", e)))?;

        chart
            .configure_mesh()
            .disable_mesh()
            .draw()
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{:?}", e)))?;

        // Scatter points
        chart
            .draw_series(
                points
                    .iter()
                    .zip(result.iter())
                    .map(|(&(x, y), &inside)| {
                        let color = if inside { GREEN } else { RED };
                        Circle::new((x, y), 1, color.filled())
                    }),
            )
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{:?}", e)))?;

        // Close polygon
        let mut poly = polygon.clone();
        if let Some(first) = polygon.first() {
            poly.push(*first);
        }

        chart
            .draw_series(std::iter::once(PathElement::new(poly, &BLUE)))
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{:?}", e)))?;

        root.present()
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{:?}", e)))?;
    }

    Ok(())
}

#[pymodule]
fn plot_polygons_rs(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(visualize_rs, m)?)?;
    Ok(())
}
