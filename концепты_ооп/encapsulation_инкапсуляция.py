# Инкапсуляция это связывание в одном объекте данных и поведения
# то есть методов работы с этими данными

class A:
    def __init__(self, a): # конструктор класса
        self.a = a # поля класса

    def show(self): # метод объекта
        print(self.a) # self-ссылка на объект

    def add(self, b):
        self.a += b


b = A(3)
b.show()
b.add(5)
b.show()

