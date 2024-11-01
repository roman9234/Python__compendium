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
        print(x**2)

    async def long_operation(text):
        # Длинная корутина
        # Которая печатает текст с задержкой 3 секунды
        print(f"Начало работы задачи: {text}")
        await asyncio.sleep(3)
        print(f"Конец работы задачи: {text}")

    async def main():


        await simple_msg("Сообщение 1") # Работа двух мгновенных корутин
        await square(10)

        # await long_operation("Задача 1") # Работа корутины с задержкой
        task = asyncio.create_task(long_operation("Задача 1"))

        await simple_msg("Сообщение 2") # Работа двух мгновенных корутин
        await square(5)

        # Объекты типа task позволяют вызвать выполнение желаемого действия в любой момент времени
        await task



    asyncio.run(main())

operations_order()























