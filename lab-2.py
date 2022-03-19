from PIL import ImageDraw

from decorators import save_image


@save_image(200, 200, 'lab-2-1')
def digital_differential_analyzer(x1: int, y1: int, x2: int, y2: int, drawer: ImageDraw) -> None:
    """
    Функция для отрисовки прямой, имея координаты начала и конца прямой

    :param x1: Координата X точки начала прямой
    :param y1: Координата Y точки начала прямой
    :param x2: Координата X точки конца прямой
    :param y2: Координата Y точки конца прямой
    :param drawer: Объект, отрисовывающий картинку
    """
    slope = (y2 - y1) / (x2 - x1)
    x = x1
    y = y1 + 0.5

    while x <= x2:
        drawer.point((x, int(y)), fill='black')
        y += slope
        x += 1


@save_image(200, 200, 'lab-2-2')
def bresenham(x1: int, y1: int, x2: int, y2: int, drawer: ImageDraw) -> None:
    """
    Функция для отрисовки прямой, имея координаты начала и конца прямой

    :param x1: Координата X точки начала прямой
    :param y1: Координата Y точки начала прямой
    :param x2: Координата X точки конца прямой
    :param y2: Координата Y точки конца прямой
    :param drawer: Объект, отрисовывающий картинку
    """
    dx = x2 - x1
    dy = y2 - y1
    e = 2 * dy - dx
    incr_e = 2 * dy
    incr_ne = incr_e - 2 * dx

    x = x1
    y = y1
    drawer.point((x, y), fill='black')

    for _ in range(dx):
        if e > 0:
            y += 1
            e += incr_ne
        else:
            e += incr_e
        x += 1
        drawer.point((x, y), fill='black')


@save_image(200, 200, 'lab-2-3')
def circle_with_digital_differential_analyzer(drawer: ImageDraw):
    pass


@save_image(200, 200, 'lab-2-4')
def circle_with_bresenham(drawer: ImageDraw):
    pass


def main() -> None:
    """
    Дата: 19.03.2022

    Описание: Рекомендуется реализовать растровые алгоритмы
    с помощью программы из первого упражнения.
    """
    digital_differential_analyzer(x1=0, y1=0, x2=100, y2=150)
    bresenham(x1=0, y1=0, x2=100, y2=200)
    circle_with_digital_differential_analyzer()
    circle_with_bresenham()


if __name__ == '__main__':
    main()
