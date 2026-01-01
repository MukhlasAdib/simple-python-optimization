import numpy as np
from numba import njit
from PIL import Image


@njit
def _compute_watermark(
    photo_pixels: np.ndarray, logo_pixels: np.ndarray, alpha: float
) -> np.ndarray:
    result = photo_pixels * (1 - alpha) + logo_pixels * alpha
    result = 0.299 * result[:, :, 0] + 0.587 * result[:, :, 1] + 0.114 * result[:, :, 2]
    return result


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = np.array(photo)
    logo_pixels = np.array(logo)
    result = _compute_watermark(photo_pixels, logo_pixels, alpha)
    return Image.fromarray(result.astype(np.uint8), "L")
