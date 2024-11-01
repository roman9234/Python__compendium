import datetime
import random
import threading
import time


# Класс Timer
# Позволяет обеспечить задержку перед исполнением функции
def class_timer():
    def gift_prepare_1(_time_interval):
        print(f"Для вас подарок! будет готов через {_time_interval} секунд...")

    def gift_ready_1():
        print("Подарок готов!")

    time_interval = 5
    gift_prepare_1(time_interval)
    send_gift_thread = threading.Timer(interval=time_interval, function=gift_ready_1)
    send_gift_thread.start()


# class_timer()


# Класс Event
# Что если два разных потока пытаются получить доступ к одним и тем же данным?
# класс Event позволяет решить эту проблему
# класс Event позволяет оповещать основной поток, было ли какое-то условие выполнено

# Рассылаем подарки, только когда их 5 штук
def class_event():
    event = threading.Event()

    def gifts_sent():
        # Изначальное состояние экземпляра класса Event False
        # пока состояние False, всё что ниже wait() не начнётся
        event.wait()
        print(f"Подарок для {threading.current_thread().name} отправлен")

    print("Отправка подарков 5 пользователям")
    for user in range(5):
        gift_prep = threading.Thread(target=gifts_sent, name=f"Пользователь {user}")
        gift_prep.start()
        print(f"Подарок пользователю {user} готов!")
        time.sleep(1)

    if threading.active_count() >= 5:
        event.set()  # переводит wait() в состояние True


# Последовательность потоков не определена

# class_event()


# Синхронизация потоков. Класс Semaphore
# Что если два разных потока пытаются работать в одно и то же время?
# Мы помним, что одновременная / параллельная работа потоков
# занимает больше времени, чем последовательная.
# Теперь на примере кода разберем, как контролировать начало и конец работы потоков.

def class_semaphore():
    class GiftsSend:
        def __init__(self):
            # Создаём экземпляр класса Semaphore
            self.moment_count = threading.Semaphore(value=2)

        def gift_send(self, winner):
            # Начинаем работу потока
            # Выделяем место новому потоку с помощью класса Semaphore()
            print(f"Оповещаем победителя {winner}")
            self.moment_count.acquire()

            # Имитируем затрату времени на отправку
            print(f"Формируем подарок для {winner}")
            time.sleep(3)
            print(f"Сейчас нет свободных мест")

            # Отправляем подарок и освобождаем место новому потоку вместо старого Semaphore
            print(f"Отправляем подарок для {winner}")
            self.moment_count.release()

        def gift_winners(self, count):
            # Формируем количество потоков по числу переданных победителей
            for winner in range(count):
                threading.Thread(target=self.gift_send, args=[winner]).start()

    g = GiftsSend()
    g.gift_winners(5)


# class_semaphore()

# Синхронизация потоков. Класс Barrier
# Как реализовать программу, которая начинает целевое действие лишь после того, как все потоки
# достигли определенного состояния?

# Задаё определённое условие, к которому должны прийти все потоки

def class_barrier():
    class GiftsSend:
        def __init__(self, count_winners):
            # Передаём число победителей
            self.count_winners = count_winners
            # Создаём экземпляр класса барьер
            self.barrier = threading.Barrier(self.count_winners)

        def gift_send(self, winner):
            # Установим разное время на сбор подарка для каждого победителя
            # Таким образом пока все подарки не собраны, мы их не отправим
            print(f"Собираем подарок для {winner}")
            # Имитируем разное время на подготовку каждого подарка
            time.sleep(random.randint(1, 13))

            print(f"Подарок для {winner} собран в {datetime.datetime.now()}")
            # Пока все потоки не упрутся в .wait() выполнение функции не продолжится
            self.barrier.wait()

            print(f"\nОтправлен подарок для {winner}, в {datetime.datetime.now()}")

    # Здесь для примера потоки будут вне класса
    first_send = GiftsSend(3)
    for winner in range(first_send.count_winners):
        threading.Thread(target=first_send.gift_send, args=str(winner)).start()


# class_barrier()


# Синхронизация потоков. Класс Lock
# Поговорим о проблеме доступа двух потоков к одной и той же переменной одновременно.
# Обсудим, почему это вообще является проблемой, и напишем код, который поможет это решить.

# Если несколько потоков могут менять одну и ту же переменную,
# то нужно предусмотреть возможность блокировки дотсупа к этой переменной то для одного,
# то для второго потока по очереди

# Без класса Lock код ниже мог бы выдать ошибку при одновременной записи имени в одну ячейку

def class_lock():
    class ListOfUsers:
        def __init__(self):
            # Устанавливаем список начальных пользователей
            self.list_of_names = ["Иван", "Вася", "Мария", "Анна"]
            # Создаём экземпляр класса Lock
            self.locker = threading.Lock()

        def new_name(self, user_name: str):
            # Блокируем доступ для остальных потоков
            self.locker.acquire()
            print(f"Новый пользователь - {user_name}")
            # Имитируем задержку, происходит context switch
            time.sleep(2)
            self.list_of_names.append(user_name)
            print(f"Пользователь {user_name} Добавлен")
            print(f"Список пользователей после - {self.list_of_names}")
            # Открываем поток, теперь есть место для нового пользователя
            self.locker.release()


    lock_example = ListOfUsers()
    print(f"Список пользователей в начале: {lock_example.list_of_names}")
    possible_names = ["Игорь", "Виталий", "Катя", "Даша", "Таня", "Стас"]

    for _ in range(3):
        new_name = random.choice(possible_names)
        threading.Thread(target=lock_example.new_name, args=[new_name]).start()

# class_lock()










