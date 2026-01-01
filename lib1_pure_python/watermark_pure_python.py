from PIL import Image


def watermarking(photo: Image.Image, logo: Image.Image, alpha: float) -> Image.Image:
    photo_pixels = list(photo.getdata())
    logo_pixels = list(logo.getdata())
    result = []

    for (pr, pg, pb), (lr, lg, lb) in zip(photo_pixels, logo_pixels):
        r = int(pr * (1 - alpha) + lr * alpha)
        g = int(pg * (1 - alpha) + lg * alpha)
        b = int(pb * (1 - alpha) + lb * alpha)
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        result.append(gray)

    out_img = Image.new("L", photo.size)
    out_img.putdata(result)
    return out_img
