# Decorator — объект, который позволяет динамически добавлять функции определенный тип поведения.

# Функции, которые изменяют поведение других функций

# особенно полезны при добавлении функциональности кеширования, логгирования, аутентификации

# декораторы стоит делать простыми - сфокусированными только на одной задаче
# использовать их стоит для повторно используемого кода
# не стоит делать слишком много декораторов для одной функции




# Пример логгирования:
def log(func):
    def wrapper(*args, **kwargs):
        print(f"calling function {func.__name__}")
        _result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {_result}")
        return _result

    return wrapper


@log
def my_func(x, y):
    return x + y


result = my_func(4, 3)




# Пример - измеряем время выполнения

import time


# Определяем функцию декоратора time_it
def time_it(func):
    # определяем функцию-оболочку, которая будет использоваться для украшения исходной функции
    # для wrapper func - это внешняя переменная, которая вызывается с параметрами
    def wrapper(*args, **kwargs):
        _start_time = time.time()
        # вызываем функцию с аргументами и аргументами по ключевым словам
        _result = func(*args, **kwargs)
        _end_time = time.time()
        # результат замера времени
        print(f"Function {func.__name__} took {_end_time - _start_time} seconds to run")
        return _result

    # возвращаем декоратор - функция wrapper
    # он будет использоваться для декорирования исходной функции
    return wrapper


# Функция my_slow_func декорирована синтаксисом @time_it, что означает, что она будет обернута декоратором time_it и это значит что будет напечатано время ее выполнения.
@time_it
def my_slow_func(x, y):
    time.sleep(2)
    return x + y


result = my_slow_func(2, 5)
