# 1 расчёт факториала
from functools import reduce

factorial = lambda n: reduce(lambda x,y: x*y, range(1,n+1))
print(factorial(5)) # 120

# 2 применение функции к каждому элементу списка

apply_to_list = lambda f, lst: [f(x) for x in lst]
print(apply_to_list(lambda x: x*2, [1,2,3,4,5])) # [2, 4, 6, 8, 10]

# 3 суммирует все аргументы при каждом вызове
# суммирует переданные функции параметры с суммой предыдущих
def partial_sum(*args):
    total = [sum(args)]
    def inner(*more_args):
        total[0] += sum(more_args)
        return total[0]
    # возвращает новую функцию, в которой можно хранить данные
    return inner

sum_func = partial_sum(1,2,3)
print(sum_func(0)) # 6
print(sum_func(5, 10)) # 21
print(sum_func(5)) # 26



















