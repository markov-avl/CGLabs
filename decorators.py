from PIL import Image, ImageDraw


def save_image(width: int, height: int, name: str) -> ():
    def outer_wrapper(function: ()) -> ():
        def inner_wrapper(*args, **kwargs) -> None:
            image = Image.new('RGB', (width, height), 'white')
            drawer = ImageDraw.Draw(image)
            function(*args, **kwargs, drawer=drawer)
            image.save(f'result/{name}.png')
        return inner_wrapper
    return outer_wrapper
