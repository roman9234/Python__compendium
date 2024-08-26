# TODO переделать проект в хранилище синтаксиса python

# Класс, от которого наследуют, называется родительским или базовым
# Класс, который наследует другой класс, называют дочерним или производным

# Простой пример класса и объекта

class A:  # описание класса
    a = 3

    def __init__(self, a):  # конструктор класса
        self.a = a  # поля класса


# ---- Наследование ----
class B(A):
    def __init__(self, a):
        # вызов конструктора суперкласса
        super().__init__(a)
        self.b = 2


b = A(5)  # создание объекта из класса
q = B(10)
print(q.a, q.b)


# ---- Уровни наследовани я от более абстрактного к полее конкретному ----

class User:
    name = ''
    email = ''
    approved_by = ''

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print("Name: ", self.name)
        print("Email:", self.email)
        print("Approved by: ", self.approved_by)
        print()


class AdminUser(User):
    def __init__(self, name, email):
        # super возвращает все поля и методы класса-родителя
        super().__init__(name, email)
        # Мы можем изменять эти атрибуты
        self.approved_by = "admin"

    def approve(self, _user: User):
        # какого пользователя нас админ проверил
        _user.approved_by = self.name


user = User('aleks', 'mail@alex.com')
user.show()
admin = AdminUser('ivan', 'mail@ivan.com')
admin.approve(user)
user.show()