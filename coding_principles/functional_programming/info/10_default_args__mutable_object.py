# Функция с аргументами по умолчанию - функция, которая позволяет указывать
# значения по умолчанию для аргументов. Удобный способ управстить вызов функции

def greet(_name='John'):
    print(f"Hello, {_name}")


greet()  # Hello, John
greet("Kate")  # Hello, Kate


# Mutable object
# Если вы используете изменяемый объект (список, словарь) в качестве аргумета по умолчанию,
# то один и тот же объект будет использоваться при все вызовах функции
# это может привести к последствиям, если объект будет изменён в функции

def add_item(item, lst=[]):
    lst.append(item)
    return lst


print(add_item(1))  # 1
print(add_item(2))  # 1, 2
print(add_item(3))  # 1, 2, 3


# Избежать ошибки можно используя неизменяемые объекты, например кортежи.

# Значение None
# Чтобы избежать проблемы вызванной мутабульностью, можно использовать значение None
# в качестве аргумента по умолчанию, и создать новый список уже внутри функции, если аргумент равен None

def add_item_not_mutable(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(add_item_not_mutable(1))  # 1
print(add_item_not_mutable(2))  # 2
print(add_item_not_mutable(3, [4]))  # 4, 3
