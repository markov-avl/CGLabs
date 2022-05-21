import numpy as np
from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plt


def B(x, k, i, t):
    if k == 0:
        return 1.0 if t[i] <= x < t[i + 1] else 0.0
    if t[i + k] == t[i]:
        c1 = 0.0
    else:
        c1 = (x - t[i]) / (t[i + k] - t[i]) * B(x, k - 1, i, t)
    if t[i + k + 1] == t[i + 1]:
        c2 = 0.0
    else:
        c2 = (t[i + k + 1] - x) / (t[i + k + 1] - t[i + 1]) * B(x, k - 1, i + 1, t)
    return c1 + c2


def bspline(x, t, c, k):
    n = len(t) - k - 1
    assert (n >= k + 1) and (len(c) >= n)
    return sum(c[i] * B(x, k, i, t) for i in range(n))


def task_1():
    """
    Реализовать интерактивную среду демонстрации
    параметрических кубических кривых (выполнять интерполяцию
    по нескольким точкам, использовать uniform B-spline и сплайн
    Катмула-Рома). Дополнительное задание: реализовать
    изменение весов точек и визуализацию рациональными
    кривыми.
    """


if __name__ == '__main__':
    # k = 3
    # t = [0, 1, 2, 3, 4, 5, 6, 2]
    # c = [-1, 2, 0, -1, -3]
    #
    # import matplotlib.pyplot as plt
    #
    # fig, ax = plt.subplots()
    # xx = np.linspace(1.5, 4.5)
    # print(xx)
    # ax.plot(xx, [bspline(x, t, c, k) for x in xx], 'r-', lw=3, label='naive')
    # # ax.plot(xx, spl(xx), 'b-', lw=4, alpha=0.7, label='BSpline')
    # ax.plot(xx, xx, 'b-', lw=3, label='andrewsha')
    # ax.grid(True)
    # ax.legend(loc='best')
    # plt.show()

    # image = Image.new('RGB', (500, 500), 'white')
    # drawer = ImageDraw.Draw(image)
    #
    # x = 0
    # y = math.sin(x)
    # while x <= 499:
    #     new_x = x + 1
    #     new_y = math.sin(new_x)
    #     drawer.line((x, y + 250, new_x, new_y + 250), fill='black')
    #     x = new_x
    #     y = new_y

    import matplotlib
    matplotlib.use('Qt5Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    xx = np.linspace(-10, 10, 1000)
    ax.plot(xx, [math.sin(x) for x in xx], 'r-', lw=3, label='naive')
    ax.grid(True)
    ax.legend(loc='best')
    # plt.show()

    plt.savefig('figures/fig1.png')
