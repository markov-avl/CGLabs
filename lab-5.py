import numpy as np
import math
import matplotlib.pyplot as plt


# https://github.com/thibauts/b-spline
def interpolate(t: float, degree: int, points: list, knots: list = None, weights: list = None) -> list:
    n = len(points)
    d = len(points[0])  # point dimensionality

    if degree < 1:
        raise Exception('degree must be at least 1 (linear)')
    if degree > n - 1:
        raise Exception('degree must be less than or equal to point count - 1')

    if weights is None:
        # build weight vector of length [n]
        weights = [1 for _ in range(n)]

    if knots is None:
        # build knot vector of length [n + degree + 1]
        knots = [i for i in range(n + degree + 1)]
    elif len(knots) != n + degree + 1:
        raise Exception('bad knot vector length')

    domain = [degree, len(knots) - 1 - degree]

    # remap t to the domain where the spline is defined
    low = knots[domain[0]]
    high = knots[domain[1]]
    t = t * (high - low) + low

    if t < low or t > high:
        raise Exception('out of bounds')

    # find s (the spline segment) for the [t] value provided
    s = domain[0]
    while not (t >= knots[s] and t <= knots[s + 1]):
        s += 1

    # convert points to homogeneous coordinates
    vector = []
    for i in range(n):
        vector.append(list())
        for j in range(d):
            vector[i].append(points[i][j] * weights[i])
        vector[i].append(weights[i])

    # l (level) goes from 1 to the curve degree + 1
    for level in range(1, degree + 2):
        # build level l of the pyramid
        for i in range(s, s - degree - 1 + level, -1):
            alpha = (t - knots[i]) / (knots[i + degree + 1 - level] - knots[i])
            # interpolate each component
            for j in range(d + 1):
                vector[i][j] = (1 - alpha) * vector[i - 1][j] + alpha * vector[i][j]

    # convert back to cartesian and return
    return [vector[s][i] / vector[s][d] for i in range(d)]


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
    save = 'result/fig1.png'

    points = [
        [-1.0, 0.0],
        [-0.5, 0.5],
        [0.5, -0.5],
        [1.0, 1]
    ]
    degree = 2

    t = float()
    x = list()
    y = list()
    while t < 1:
        point = interpolate(t, degree, points)
        x.append(point[0])
        y.append(point[1])
        t += 0.01

    fig, ax = plt.subplots()
    xx = np.linspace(-10, 10, 1000)
    ax.scatter([point[0] for point in points], [point[1] for point in points], c='r')
    ax.plot(x, y, 'g-', lw=3, label='uniform b-spline')
    ax.grid(True)
    ax.legend(loc='best')

    plt.savefig(save)