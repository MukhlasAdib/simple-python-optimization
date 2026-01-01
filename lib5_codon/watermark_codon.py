import numpy as np
from PIL import Image

from .image_proc import compute_watermark


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = np.array(photo)
    logo_pixels = np.array(logo)
    result = compute_watermark(photo_pixels, logo_pixels, alpha)
    return Image.fromarray(result.astype(np.uint8), "L")
