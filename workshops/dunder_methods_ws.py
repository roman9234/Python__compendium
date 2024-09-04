# Реализация точки на координатной плоскости

import math
from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __repr__(self):
        # метод должен возвращать корректный python код
        return f'Point(x={self._x},y={self._y})'
    def __abs__(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __eq__(self, other):
        return hash(self) == hash(other)
    def __hash__(self):
        return hash(abs(self))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __add__(self, other):
        return Point(x = self._x + other._x, y = self._y + other._y)

    def __sub__(self, other):
        return Point(x=self._x - other._x, y=self._y - other._y)

    def __mul__(self, other):
        return Point(x=self._x * other._x, y=self._y * other._y)

    # Унарные операции

    def __pos__(self):
        return Point(x = +self._x, y=+self._y)

    def __neg__(self):
        return Point(x = -self._x, y=-self._y)

    def __invert__(self):
        return Point(x = self._y, y=self._x)

    # Опреации преобразования
    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return float(abs(self))

    def __round__(self, n=None):
        return round(abs(self), n)


p1 = Point(1,5)

print(p1)
# Модуль
print(abs(p1))
# сравнение
p2 = Point(-1, 5)
print(p1 == p2)
# функиця hash (только для неизменяемых объектов)
print()
print(Point(2,2) < Point(1,1))
print(Point(2,2) <= Point(1,1))
print(Point(2,2) > Point(1,1))
print(Point(2,2) >= Point(1,1))
print(Point(2,2) >= Point(2,2))
print(Point(2,2) >= Point(2,3))
# сложение вычитание умножение
print()
print(Point(2,2) + Point(2,-1))
print(Point(2,2) - Point(2,-1))
print(Point(2,2) * Point(2,-1))
# Унарные операции
print()
print(-Point(2,2))
print(+Point(2,2))
print(~Point(2,5))
print()
print(int(Point(3,4)))
print(float(Point(3,4)))
print(float(Point(2,4)))
print(round(Point(2,4), 4))
