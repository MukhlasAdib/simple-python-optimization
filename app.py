from PIL import Image
from pyinstrument import Profiler

from lib1_pure_python import watermark_pure_python
from lib2_numpy import watermark_numpy
from lib3_opencv import watermark_opencv
from lib4_numba import watermark_numba
from lib5_codon import watermark_codon
from lib6_codon_jit import watermark_codon_jit
from lib7_numpy_v2 import watermark_numpy_v2
from lib8_codon_v2 import watermark_codon_v2
from lib9_codon_v3 import watermark_codon_v3

PHOTO_PATH = "images/photo.jpg"
LOGO_PATH = "images/duck_logo.png"
IMAGE_SIZE = (1280, 720)

watermarking = watermark_codon_v3.watermarking


def main():
    photo = Image.open(PHOTO_PATH).convert("RGB")
    logo = Image.open(LOGO_PATH).convert("RGB")
    alpha = 0.2

    for _ in range(3):
        watermarking(photo, logo, alpha)

    profiler = Profiler()
    profiler.start()
    for _ in range(5):
        result_image = watermarking(photo, logo, alpha)
    profiler.stop()
    print(
        profiler.output_text(
            unicode=True,
            color=True,
            show_all=True,
        )
    )

    result_image.save("output.png")


if __name__ == "__main__":
    main()
