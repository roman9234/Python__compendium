# Dunder методы
# dunder - double underscore
# методы, название которых начинается и заканчивается с двух нижних подчеркиваний, например __init__, __str__, __ge__ и т.д.
# также их называют магическими методами
# в документации - special methods

class SomeClass:
    def __init__(self, value):
        print("вызов метода __init__")
        self._value = value

    def __eq__(self, other):
        print("вызов метода __eq__")
        return hash(self._value) == hash(other._value)

    def equals(self, other):
        print("вызов метода __eq__")
        return hash(self._value) == hash(other._value)


a = SomeClass(1)
c = SomeClass(1)

if a.equals(c):
    print("is equals")

if a == c:
    print("is equals with ==")


# Операторы сравнения

class SomeClass1:
    def __init__(self, value) -> None:
        self._value = value

    def __eq__(self, other):
        return hash(self._value) == hash(other._value)

    def __lt__(self, other):
        return self._value < other._value


a = SomeClass1(1)
b = SomeClass1(2)
print(a < b)
# True
print(a.__lt__(b))
# True
print(a > b)
# False
print(a.__gt__(b))
# NotImplemented
# print(a <= b)
# # NotImplemented

# Если в классе определены несколько методов расширенного
# сравнения, этот декоратор предоставит все остальные.
# Это упрощает работу по определению всех возможных операций сравнения.

from functools import total_ordering


# теперь достаточно определить только 2 метода - равно + сравнение
@total_ordering
class SomeClass:
    def __init__(self, value) -> None:
        self._value = value

    def __eq__(self, other):
        return hash(self._value) == hash(other._value)

    def __lt__(self, other):
        return self._value < other._value


a = SomeClass(1)
b = SomeClass(2)
print(a > b)
# False
print(a.__gt__(b))


# False


# ---- отражённые операции и расширенное присвоение ----

class SomeClass:

    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        return type(self)(self._value + other._value)

    def __iadd__(self, other):
        print('Вызов метода __iadd__')
        self._value = self._value + other._value
        return self


class SomeOtherClass(SomeClass):
    def __rsub__(self, other):
        print('Вызов метода __rsub__')
        return type(other)(other._value - self._value)


a, b = SomeClass(4), SomeOtherClass(2)
print(a)
# <__main__.SomeClass object at 0x107634fd0>
print(a + b)
# <__main__.SomeClass object at 0x107634d90>
a += b
# Вызов метода __iadd__
print(a)
# <__main__.SomeClass object at 0x107634fd0>
c = a - b
# Вызов метода __rsub__
print(c._value)
# 4

# Методы преобразования

import string


class Letter:
    def __init__(self, value):
        self._value = value

    def __index__(self):
        print('Вызов метода __index__')
        return self._value - 1


ltt = Letter(3)
alphabet = list(string.ascii_uppercase)
print(alphabet[ltt])
# Вызов метода __index__
# C

# ---- Методы представления ----

import datetime

print(repr(object))
# <class ‘object’>
now = datetime.datetime.now()
print(repr(now))
# datetime.datetime(2023, 3, 27, 14, 29, 4, 256282)
print(str(now))


# 2023-03-27 14:29:04.256282

# ---- Доступ к аттрибутам ----

class C:
    def __len__(self): return 10

    def __getattribute__(*args):
        print('Вызов метода __getattribute__')
        return object.__getattribute__(*args)


c = C()
print(c.__len__())
# Вызов метода __getattribute__
# 10
print(len(c))


# 10

# ---- Классы дескрипторы ----

class CounterDescriptor:
    def __init__(self, value):
        self._value = value
        self._counter = 0

    def __get__(self, instance, owner=None):
        print('Вызов метода __get__')
        self._counter += 1
        return (self._value, self._counter)

    def __set__(self, instance, value):
        self._counter = 0
        self._value = value


class ClassWithDescriptor:
    x = CounterDescriptor(10)

print("классы дискрипторы")
f = ClassWithDescriptor()
f.x
# Вызов метода __get__
f.x
# Вызов метода __get__
print(f.x)
# Вызов метода __get__
# (10, 3)
f.x = 11
print(f.x)
# Вызов метода __get__
# (11, 1)
