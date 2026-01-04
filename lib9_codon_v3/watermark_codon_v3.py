import inspect

import numpy as np
from PIL import Image

from .image_proc import compute_watermark

fn = compute_watermark

print("type:", type(fn))
print("repr:", fn)
print("callable?", callable(fn))
try:
    print("signature via inspect:", inspect.signature(fn))
except Exception as e:
    print("inspect.signature failed:", e)

print("\nAttributes that might show overloads:")
for name in (
    "__overloads__",
    "overloads",
    "signatures",
    "_signatures",
    "_overloads",
    "_kernels",
    "_impls",
    "_dispatch",
    "__callables__",
    "dispatch",
):
    if hasattr(fn, name):
        print(name, "=", getattr(fn, name))
print("\nSome dir() entries:")
print([x for x in dir(fn) if not x.startswith("_")][:80])


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = np.array(photo)
    logo_pixels = np.array(logo)
    result = compute_watermark(photo_pixels, logo_pixels, alpha)
    return Image.fromarray(result.astype(np.uint8), "L")
