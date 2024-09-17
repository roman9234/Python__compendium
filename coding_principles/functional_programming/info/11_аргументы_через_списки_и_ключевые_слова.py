# Списки аргументов и ключевых слов
# это воможность, которая позволяет функциям принимать произвольное количество аргументов либо в виде списка,
# либо в качестве аргументов по ключевым словам

# полезно при работе с функциями, которые принимают переменное значение аргументов


# Распаковка ргументов
# используем оператор * для распаковки списка и передачи его содержимого в качестве аргументов функции

def add_numbers_1(*args):
    return sum(args)


numbers = [1, 2, 2, 1]
print(add_numbers_1(*numbers))  # 6


def add_numbers_2(x, y, z):
    return x + y + z


numbers = [1, 3, 21]
print(add_numbers_2(*numbers))  # 25


# используем оператор ** для распаковки словаря
# и передачи его содержимого в качестве аргументов по ключевым словам в функцию

def print_person_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


person = {"name": "Alice", "age": 30, "city": "New York"}
print_person_info(**person)


# Переменное количество аргументов
# Это возможность, которая позволяет функциям принимать произвольное количество аргументов
# либо в виде списка, либо в качестве аргументов по ключевым словам

# *args синтаксис
# Мы можем передать функции любое количество аргументов,
# и они будут собраны в кортеж под названием args.
# Внутри функции мы можем перебирать кортеж args и складывать числа

def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total


print(sum_numbers(5, 5, 10, 20))  # 40


# Позиционные аргументы
# мы можем использовать обычные позиционные аругменты совместно с *args синтаксисом

def print_names(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")


print_names("Hello", "Alice", "Bob", "Charlie")


# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

# С ключевыми словами
# синтаксис kwargs также позволяет передавать в функцию переменное количество аргументов

def print_persons_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_persons_info(name='Alice', age=30, city="New York")
# name: Alice
# age: 30
# city: New York

# сначала будут применяться аргументы по умолчанию, затем *args и **kwargs
