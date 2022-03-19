from typing import Iterator


class Point:
    def __init__(self, x: int | float, y: int | float) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int | float:
        return self._x

    @x.setter
    def x(self, value) -> None:
        self._x = value

    @property
    def y(self) -> int | float:
        return self._y

    @y.setter
    def y(self, value) -> None:
        self._y = value

    def normalized(self):
        return Point(int(self._x), int(self._y))

    def __iter__(self) -> Iterator[int | float]:
        yield self._x
        yield self._y

    def __getitem__(self, item) -> int | float:
        return list(self)[item]

    def __len__(self) -> int:
        return 2


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self._start = start
        self._end = end

    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, value) -> None:
        self._start = value

    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, value) -> None:
        self._end = value

    def normalized(self):
        return Line(self.start.normalized(), self.end.normalized())

    def __iter__(self) -> Iterator[int | float]:
        yield self._start.x
        yield self._start.y
        yield self._end.x
        yield self._end.y

    def __getitem__(self, item) -> int | float:
        return list(self)[item]

    def __len__(self) -> int:
        return 4
