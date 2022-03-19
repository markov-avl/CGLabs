import math
from PIL import ImageDraw

from decorators import save_image
from models import Point, Line


@save_image(200, 200)
def draw_lines_with_angle(point: Point, length: int, angle: int, drawer: ImageDraw) -> None:
    """
    Функция для отрисовки двух прямых под углом

    :param point: Координата точки начала прямых
    :param length: Длина прямых
    :param angle: Величина угла в градусах
    :param drawer: Объект, отрисовывающий картинку
    """
    # переводим угол в радианы
    angle_rad = angle / 180 * math.pi

    # первая линия отрисовывается горизонтально, а вторая - под углом angle
    for alpha in (0, angle_rad):
        line = Line(point, Point(point.x + math.cos(alpha) * length, point.y + math.sin(alpha) * length))
        # отрисовываем линию под углом alpha
        drawer.line(line, fill='black', width=1)


def main() -> None:
    """
    Дата: 05.03.2022

    Описание: Написать функцию для отрисовки двух прямых под углом,
    функция должна принимать на вход начальную точку, угол и длину прямых
    """
    draw_lines_with_angle(point=Point(100, 100), length=100, angle=100)


if __name__ == '__main__':
    main()
