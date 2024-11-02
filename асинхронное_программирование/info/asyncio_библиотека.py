import asyncio
import time


# async - асинхронность
# io - I/O Bound


# В случие асинхронного программирования мы используем не функции а курутины
# Это обычные функции, перед которыми стоит ключевое слово async

def async_demonstration():
    async def async_func():
        print(1)
        await asyncio.sleep(1)
        print(2)

    async def main():
        await asyncio.gather(async_func(), async_func())

    asyncio.run(main())


# async_demonstration()

# Асинхронные циклы for

# Синхронный подход
def sync_approach():
    def func(arg_1_1):
        for n in range(arg_1_1):
            yield n
            time.sleep(1)

    def run(arg_1_2):
        for i in func(arg_1_2 + 1):
            print(i)
            print("sleep(1)")

    def main():
        start_time = time.time()
        run(1)
        run(2)
        finish_time = time.time()
        release_time = finish_time - start_time
        print(release_time)

    main()


def async_approach():
    async def func(arg_1_1):
        for n in range(arg_1_1):
            yield n
            await asyncio.sleep(1)

    async def run(arg_1_2):
        async for i in func(arg_1_2 + 1):
            print(i)
            print("asyncio.sleep(1)")

    async def main():
        start_time = time.time()
        await asyncio.gather(run(2), run(1))
        finish_time = time.time()
        release_time = finish_time - start_time
        print(release_time)

    asyncio.run(main())


# sync_approach()
# async_approach()
# Время работы программы - время работы самой длинной из функций


# Порядок выполнения процессов
# Важен если корутины зависят друг от друга
# Или взаимодействуют с одними и теми же переменными

def operations_order():
    async def simple_msg(message):
        # Быстрая корутина, которая печатает сообщение
        print(message)

    async def square(x):
        # Быстрая корутина которая печатает число, возведённое в квадрат
        print(x ** 2)

    async def long_operation(text):
        # Длинная корутина
        # Которая печатает текст с задержкой 3 секунды
        print(f"Начало работы задачи: {text}")
        await asyncio.sleep(3)
        print(f"Конец работы задачи: {text}")

    async def main():
        await simple_msg("Сообщение 1")  # Работа двух мгновенных корутин
        await square(10)

        # await long_operation("Задача 1") # Работа корутины с задержкой
        task = asyncio.create_task(long_operation("Задача 1"))

        await simple_msg("Сообщение 2")  # Работа двух мгновенных корутин
        await square(5)

        # Объекты типа task позволяют вызвать выполнение желаемого действия в любой момент времени
        await task

    asyncio.run(main())


# operations_order()


# Состояния процессов

# В этом блоке мы поговорим про возможные состояния задач, и отдельно обсудим,
# почему важно это контролировать. С помощью Python и библиотеки asyncio попробуем ускорить работу асинхронных процессов, манипулируя их состояниями.

# Состояния в которых могут быть задачи:

# Запущена - Running
# Не запущена или в блоке - Pending
# Завершена - Done
# Отменена - Cancelled

# Результаты можно забрать не из всех состояний, в которых находится задача
# Метод .as_completed() позволяет запускать некоторые задачи не дожидаясь завершения других

def operations_state_as_completed():
    async def simple_msg(message):
        print(message)

    async def square(x):
        print(x ** 2)

    async def long_operation(text):
        print(f"Начало работы задачи: {text}")
        await asyncio.sleep(3)
        print(f"Конец работы задачи: {text}")

    async def main():
        short_task_msg_1 = asyncio.create_task(simple_msg("Сообщение 1"))  # Работа двух мгновенных корутин
        short_task_square_1 = asyncio.create_task(square(10))

        # await long_operation("Задача 1") # Работа корутины с задержкой
        long_task_1 = asyncio.create_task(long_operation("Задача 1"))
        long_task_2 = asyncio.create_task(long_operation("Задача 2"))

        short_task_msg_2 = asyncio.create_task(simple_msg("Сообщение 2"))  # Работа двух мгновенных корутин
        short_task_square_2 = asyncio.create_task(square(5))

        # Объекты типа task позволяют вызвать выполнение желаемого действия в любой момент времени
        # Метод .as_completed() для нескольких задач
        # Короткие задачи запускаются пока ожидается выполнение длинных:
        for task in asyncio.as_completed((
                short_task_msg_1, short_task_square_1,
                short_task_msg_2, short_task_square_2,
                long_task_1, long_task_2,
        )):
            await task

    asyncio.run(main())


# Вариант с функцией wait

def operations_state_wait():
    async def simple_msg(message):
        print(message)

    async def square(x):
        print(x ** 2)

    async def long_operation(text):
        print(f"Начало работы задачи: {text}")
        await asyncio.sleep(3)
        print(f"Конец работы задачи: {text}")

    async def main():
        short_task_msg_1 = asyncio.create_task(simple_msg("Сообщение 1"))  # Работа двух мгновенных корутин
        short_task_square_1 = asyncio.create_task(square(10))

        # await long_operation("Задача 1") # Работа корутины с задержкой
        long_task_1 = asyncio.create_task(long_operation("Задача 1"))
        long_task_2 = asyncio.create_task(long_operation("Задача 2"))

        short_task_msg_2 = asyncio.create_task(simple_msg("Сообщение 2"))  # Работа двух мгновенных корутин
        short_task_square_2 = asyncio.create_task(square(5))

        # Объекты типа task позволяют вызвать выполнение желаемого действия в любой момент времени
        # Метод .as_completed() для нескольких задач
        # метод .wait показывает состояния задач, но не создаёт генератор
        done, pending = await asyncio.wait((
            short_task_msg_1, short_task_square_1,
            short_task_msg_2, short_task_square_2,
            long_task_1, long_task_2,
        ))
        print(f"Done:\n", done)
        print(f"Pending:\n", pending)

    asyncio.run(main())


# operations_state_as_completed()
# operations_state_wait()


# Манипулирование состоянием задач вручную:

def operations_state_manipulation():
    async def simple_msg(message):
        print(message)

    async def square(x):
        print(x ** 2)

    async def long_operation(text):
        print(f"Начало работы задачи: {text}")
        await asyncio.sleep(3)
        print(f"Конец работы задачи: {text}")

    async def main():
        short_task_msg_1 = asyncio.create_task(simple_msg("Сообщение 1"))  # Работа двух мгновенных корутин
        short_task_square_1 = asyncio.create_task(square(10))

        long_task_1 = asyncio.create_task(long_operation("Задача 1"))

        print(f"Результат метода done() - {long_task_1.done()}") # False
        print(f"Результат метода cancelled() - {long_task_1.cancelled()}") # False
        print(f"Результат метода cancel() - {long_task_1.cancel("Принудительная остановка")}") # True
        print()
        print("")

        # метод .wait показывает состояния задач, но не создаёт генератор
        done, pending = await asyncio.wait((
            short_task_msg_1, short_task_square_1,
            long_task_1,
        ))
        print("---")
        print(f"Done:\n", done)
        print(f"Pending:\n", pending)

        # Проверка состояний после работы метода .wait()
        print(f"Повторный результат метода done() - {long_task_1.done()}") # True
        print(f"Повторный результат метода cancelled() - {long_task_1.cancelled()}") # True

    asyncio.run(main())
# operations_state_manipulation()