from PIL import ImageDraw

from decorators import save_image
from models import Point


@save_image(200, 200)
def digital_differential_analyzer(start: Point, end: Point, drawer: ImageDraw) -> None:
    """
    Функция для отрисовки прямой, имея координаты начала и конца прямой

    :param start: Координата точки начала прямой
    :param end: Координата точки конца прямой
    :param drawer: Объект, отрисовывающий картинку
    """
    slope = (end.y - start.y) / (end.x - start.y)
    point = Point(x=start.x, y=start.y + 0.5)

    while point.x <= end.x:
        drawer.point(point.normalized(), fill='black')
        point.y += slope
        point.x += 1


@save_image(200, 200)
def bresenham(start: Point, end: Point, drawer: ImageDraw) -> None:
    """
    Функция для отрисовки прямой с помощью алгоритма Брезенхема

    :param start: Координата точки начала прямой
    :param end: Координата точки конца прямой
    :param drawer: Объект, отрисовывающий картинку
    """
    dx = end.x - start.x
    dy = end.y - start.y
    e = 2 * dy - dx
    incr_e = 2 * dy
    incr_ne = incr_e - 2 * dx

    point = Point(*start)
    drawer.point(point, fill='black')

    for _ in range(dx):
        if e > 0:
            point.y += 1
            e += incr_ne
        else:
            e += incr_e
        point.x += 1
        drawer.point(point, fill='black')


@save_image(200, 200)
def circle_with_digital_differential_analyzer(drawer: ImageDraw):
    pass


@save_image(200, 200)
def circle_with_bresenham(drawer: ImageDraw):
    pass


def main() -> None:
    """
    Дата: 19.03.2022

    Описание: Рекомендуется реализовать растровые алгоритмы
    с помощью программы из первого упражнения.
    """
    digital_differential_analyzer(start=Point(0, 0), end=Point(100, 10))
    bresenham(start=Point(0, 0), end=Point(100, 100))
    circle_with_digital_differential_analyzer()
    circle_with_bresenham()


if __name__ == '__main__':
    main()
