# 1
print("нечётные элементы")


def odd_printer(list):
    if len(list) == 0:
        return
    else:
        if list[0] % 2 != 0:
            print(list[0])
        odd_printer(list[1:])


test_list = [1, 4, 6, 9, 12, 67, 90, 103]
odd_printer(test_list)




# 2
print("подсчёт длины списка")


def els_counter(list):
    try:
        list[0]
    except IndexError:
        return 0
    return els_counter(list[1:]) + 1


test_list = [1, 4, 6, 9, 12, 67, 90, 103]
print(els_counter(test_list))




# 3
print("Вывод следующего элемента заданного списка")

current_element = 0
def next_print(list):
    global current_element
    if len(list) >= current_element:
        print(list[current_element])
        current_element+=1
    else:
        print("No next element")

test_list = [1, 4, 6, 9, 12, 67, 90, 103]
next_print(test_list)
next_print(test_list)
next_print(test_list)
next_print(test_list)

