# Полиморфизм - это способность функции принимать объекты различных типов и работать с ними обобщённо
# TODO сделать пример получше

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