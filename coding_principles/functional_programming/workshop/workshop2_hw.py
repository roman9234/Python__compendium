# 1 Палиндромы
print("Фукнция, которая оставляет только палиндромы в списке")
# можно в одну строку, но здесь с переносами для наглядности
poli_func = lambda str_list: list(
    filter(
        lambda _str: _str == _str[::-1],
        str_list
    )
)

strings = ["racecar", "hello", "deified", "lorem", "heh"]
print(poli_func(strings))
# ['racecar', 'deified', 'heh']


# 2
print("последовательность Коллатца для заданного начального числа")


# мы храним последовательность в collatz_list, используя замыкание
# inner - генератор

def collatz_conjecture(_n):
    collatz_list = [_n]

    def inner():
        while collatz_list[-1] != 1:
            if collatz_list[-1] % 2 == 0:
                collatz_list.append(collatz_list[-1] // 2)
            else:
                collatz_list.append((collatz_list[-1] * 3) + 1)
            yield collatz_list[-1]

    return inner


print(3)
generator = collatz_conjecture(3)
for i in generator():
    print(i, end=" ")
# 3 10 5 16 8 4 2 1

print("\n39")
generator = collatz_conjecture(39)
for i in generator():
    print(i, end=" ")
# 118 59 178 89 268 134 67 202 101 304 152 76 38 19 58 29
# 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1


# 3
print("каждое целое число заменено квадратным корнем, округленным до ближайшего целого числа")

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        _start_time = time.time()
        _result = func(*args, **kwargs)
        _end_time = time.time()
        print(f"Function {func.__name__} took {_end_time - _start_time} seconds to run")
        return _result

    return wrapper


from math import sqrt, ceil, floor


@time_it
def list_rooter(_lst: list, rounding_direction="down"):
    if rounding_direction == "down":
        for _i in range(len(_lst)):
            _lst[_i] = floor(sqrt(_lst[_i]))
    elif rounding_direction == "up":
        for _i in range(len(_lst)):
            _lst[_i] = ceil(sqrt(_lst[_i]))
    else:
        print(f"incorrect argument: {rounding_direction}")
        for _i in range(len(_lst)):
            _lst[_i] = ceil(sqrt(_lst[_i]))
    return _lst


testing_list = [2, 4, 9, 10, 12]
print(list_rooter(testing_list, rounding_direction="down"))
# Function list_rooter took 0.0 seconds to run
# [1, 2, 3, 3, 3]
testing_list = [2, 4, 9, 10, 12]
print(list_rooter(testing_list, rounding_direction="up"))
# Function list_rooter took 0.0 seconds to run
# [2, 2, 3, 4, 4]

testing_list = [i for i in range(2,10000000)]
list_rooter(testing_list, rounding_direction="up")
# Function list_rooter took 1.3949992656707764 seconds to run

