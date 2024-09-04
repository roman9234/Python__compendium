# Полиморфизм - это способность функции принимать объекты различных типов и работать с ними обобщённо
# способность объектов различных классов рассматриваться так,
# как если бы они были объектами одного и того же класса

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


# экземпляры класса могут влиять друг на друга
user = User('aleks', 'mail@alex.com')
user.show()
admin = AdminUser('ivan', 'mail@ivan.com')
admin.approve(user)
user.show()
admin2 = AdminUser('petr', 'mail@petr.com')
admin2.approve(admin)
admin.show()


# ---- Типы полиморфизма ----
# 1 - Полиморфизм во время компиляции - использование методов с одинаковым именем и разными списками параметров
# 2 - Полиморфизм во время выполнения - можно использовать один и тот де метод с различными объектами,
# которые могут иметь различные реализации этого метода

# ---- Перезагрузка методов ----
# форма полиморфизма во время компиляции.
# несколько методов с одним именем, но разными списками параметров

# ---- Переопределение методов ----
# форма полиморфизма во время выполнения. Позволяет классу переопределять методы суперкласса

class Shape:
    def area(self):
        pass  # abstract method that will be overridden in subclasses


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# create instances of the Square and Circle classes
s = Square(5)
c = Circle(2)
# call the area method on both objects, even though they are of different classes
print("Area of square:", s.area())
print("Area of circle:", c.area())
