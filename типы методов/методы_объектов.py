class Car:
    engine_is_running = False

    # ---- Конструктор ----
    # Вызывается автоматически при создании класса
    def __init__(self, serial_id):
        self.sID = serial_id
        print(f"car with id {self.sID} created")

    # ---- Деструктор ----
    # Отвечает за удаление всей информации объекта
    # используется для закрытия связанных с объектом файлов, подключений
    def __del__(self):
        pass


# создание экземпляра класса
car1 = Car(1)
# удаление экземпляра класса
del car1


class CarNew:
    def init(self, serial_id):
        self.sID = serial_id
        print(f"car with id {self.sID} created")


# создание экземпляра, затем вызов "конструктора" вручную
car2 = CarNew()
car2.init(1)
