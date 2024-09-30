# Инкапсуляция это связывание в одном объекте данных и поведения
# то есть методов работы с этими данными
# защита внутреннего состояния объекта
# упрощение взаимодействия объектов

class A:
    def __init__(self, a):  # конструктор класса
        self.a = a  # поля класса

    def show(self):  # метод объекта
        print(self.a)  # self-ссылка на объект

    def add(self, _b):
        self.a += _b


b = A(3)
b.show()
b.add(5)
b.show()


# ---- Модификаторы доступа ----
# используются для управления видимостью переменных и методов

# private - доступ в пределах одного метода
# обозначается знаком подчёркивания _

# protected - дотсуп в пределах производных классов. Даёт переопределять методы
# public - доступ везде

# пример: все переменные закрыты, и могут быть получены только через геттеры

class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
    def get_balance(self):
        return self._balance

