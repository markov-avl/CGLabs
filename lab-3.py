from random import randint

from PIL import ImageDraw, Image

from decorators import save_image
from models import Point


def fixed_thresholding() -> None:
    image = Image.open('source/img-0.png')
    for x in range(image.width):
        for y in range(image.height):
            if sum(image.getpixel((x, y))[0: 3]) // 3 > 128:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            image.putpixel((x, y), color)
    image.save('result/image.png')


def random_thresholding() -> None:
    image = Image.open('source/img-0.png')
    for x in range(image.width):
        for y in range(image.height):
            if sum(image.getpixel((x, y))[0: 3]) // 3 > randint(0, 255):
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            image.putpixel((x, y), color)
    image.save('result/image-1.png')


def ordered_dither() -> None:
    m = [
        [0, 2],
        [3, 1]
    ]
    image = Image.open('source/img-0.png')
    for x in range(image.width):
        for y in range(image.height):
            threshold = sum(image.getpixel((x, y))[0: 3]) // 3
            if threshold * 5 // 256 > m[x % 2][y % 2]:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            image.putpixel((x, y), color)
    image.save('result/image-2.png')


def main() -> None:
    """
    Дата: 02.04.2022

    Описание: -
    """
    # fixed_thresholding()
    # random_thresholding()
    ordered_dither()


if __name__ == '__main__':
    main()
