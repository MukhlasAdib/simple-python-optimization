from unittest import result

import numpy as np
from PIL import Image


def _compute_watermark(
    photo_pixels: np.ndarray, logo_pixels: np.ndarray, alpha: float
) -> np.ndarray:
    result = np.zeros((photo_pixels.shape[0], photo_pixels.shape[1]), dtype=np.uint8)
    for i in range(photo_pixels.shape[0]):
        for j in range(photo_pixels.shape[1]):
            r = photo_pixels[i, j, 0] * (1 - alpha) + logo_pixels[i, j, 0] * alpha
            g = photo_pixels[i, j, 1] * (1 - alpha) + logo_pixels[i, j, 1] * alpha
            b = photo_pixels[i, j, 2] * (1 - alpha) + logo_pixels[i, j, 2] * alpha
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            result[i, j] = gray
    return result


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = np.array(photo)
    logo_pixels = np.array(logo)
    result = _compute_watermark(photo_pixels, logo_pixels, alpha)
    return Image.fromarray(result.astype(np.uint8), "L")
