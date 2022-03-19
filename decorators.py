import sys
from PIL import Image, ImageDraw
from pathlib import Path


k = 0
name = Path(sys.argv[0]).name.split('.')[0]
result = Path(sys.argv[0]).parent.joinpath('result')


if not result.exists() or not result.is_dir():
    result.mkdir()


def save_image(width: int, height: int) -> ():
    def outer_wrapper(function: ()) -> ():
        def inner_wrapper(*args, **kwargs) -> None:
            global k
            k += 1
            image = Image.new('RGB', (width, height), 'white')
            drawer = ImageDraw.Draw(image)
            function(*args, **kwargs, drawer=drawer)
            image.save(result.joinpath(f'{name}-{k}.png'))
        return inner_wrapper
    return outer_wrapper
