# Каррирование - метод, который включает преобразование функции от множетва аргументов
# в набор функций, каждая из которых является функцией от одного аргумента

# может быть полезно когда функция должна быть частично применена, или аргументы должны быть гибкими и моульными

def curr_func(a):
    def tmp_func1(b):
        def tmp_func2(c):
            return a + b + c

        return tmp_func2

    return tmp_func1


print(curr_func(1)(2)(3))
