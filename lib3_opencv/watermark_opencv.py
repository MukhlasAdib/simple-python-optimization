import cv2
import numpy as np
from PIL import Image


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = np.array(photo)
    logo_pixels = np.array(logo)
    result = cv2.addWeighted(photo_pixels, 1 - alpha, logo_pixels, alpha, 0)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    return Image.fromarray(result, "L")
