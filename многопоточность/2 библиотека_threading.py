# Есть 2 типа потоков:

# Foreground поток (главный поток) — поток, завершения работы которого дожидается программа.

# Background поток (второстепенный поток) — это тот поток, завершения работы которого,
#     главная программа может не дожидаться. И если главный поток завершится раньше,
#     то он не дожидается завершения background потока, чтобы закончить выполнение всей программы.


# Context switch — процедура, когда CPU вычислительная машина переключается между одной и второй задачей.
#     Эта процедура включает в себя прекращения выполнения процессором одной задачи
#     с сохранением всей необходимой информации и состояния, необходимых для последующего продолжения с прерванного места,
#     и восстановления и загрузки состояния задачи, к выполнению которой переходит процессор.


# По умолчанию создаётся поток main()

import time


def func(x):
    star_time = time.time()
    lst = []
    for elem in range(x):
        lst.append(elem)
    end = time.time()
    print(f"Выполнено за {end - star_time}")
    return sum(lst)


# Foreground поток создаётся всегда

# Заход в главный поток по умолчанию
# print("Запуск потока main()")
# print(func(30000000))
# print("Завершение потока main()")

# Реализуем выполнение функции func() в виде отдельного потока

import threading

def func(n, x):
    start = time.time()
    lst = []
    for elem in range(x):
        lst.append(elem)

    end = time.time()
    print(f"Выполнено за {end-start}\nЗначение - {sum(lst)}")


# Заход в главный поток
print("Запуск потока main()")

# Создаём поток
# Это тоже Foreground поток
thread = threading.Thread(target=func, args=(1,3_000_000))

# Запускаем поток
thread.start()

print("Завершение потока main")

# В этом случие поток main выполняется гораздо быстрее чем функция func()








