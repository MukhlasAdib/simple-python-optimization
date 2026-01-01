import numpy as np
from PIL import Image


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = np.array(photo)
    logo_pixels = np.array(logo)
    result = photo_pixels * (1 - alpha) + logo_pixels * alpha
    result = 0.299 * result[:, :, 0] + 0.587 * result[:, :, 1] + 0.114 * result[:, :, 2]
    return Image.fromarray(result.astype(np.uint8), "L")
