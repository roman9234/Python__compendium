# Лямбда-функция
# — это анонимная функция, выраженная в виде одного оператора.

# Полезны потому что позволяют писать краткий и легко читаемый код
# Полезны при работе с функциями высокого порядка - map filter reduce и при обработке списков

# Стоит использовать только при простым набором параметров и простой логикой

# Синтаксис:
# lambda arguments: expression

double = lambda x: x * 2
print(double(2))

mylist = [2, 20, 5, 26, 35, 17, 34]
# lambda как параметр функции высшего порядка
filtered_list = list(filter(lambda x: (x % 2 == 0), mylist))
print(filtered_list)

# складываение чисел
add = lambda x, y: x + y
print(add(1, 3))

# сортировка списка кортежей (по 2 элементу)
points = [(1, 2), (3, 1), (5, 4), (2, 2)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)



