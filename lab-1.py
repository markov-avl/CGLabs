from PIL import Image, ImageDraw
import math


# создаем обьект изображения и кисть
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)


def draw_lines_with_angle(x1: int, y1: int, length: int, angle: int) -> None:
    """
    Функция для отрисовки двух прямых под углом

    :param x1: Координата X точки начала
    :param y1: Координата Y точки начала
    :param length: Длина прямых
    :param angle: Величина угла в градусах
    """
    # переводим угол в радианы
    angle_rad = angle / 180 * math.pi

    # первая линия отрисовывается горизонтально, а вторая - под углом angle
    for alpha in (0, angle_rad):
        x2 = x1 + math.cos(alpha) * length
        y2 = y1 + math.sin(alpha) * length
        # отрисовываем линию под углом alpha
        draw.line((x1, y1, x2, y2), fill='black', width=1)


def main() -> None:
    """
    Дата: 05.03.2022

    Описание: Написать функцию для отрисовки двух прямых под углом,
    функция должна принимать на вход начальную точку, угол и длину прямых
    """
    draw_lines_with_angle(x1=100, y1=100, length=100, angle=135)
    image.save('result/lab-1.png')


if __name__ == '__main__':
    main()
