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
        super().__init__(name, email)
        self.approved_by = 'admin'

    def approve(self, user:User):
        user.approved_by = self.name

user = User('aleks', 'mail@alex.com')
admin = AdminUser('ivan', 'mail@ivan.com')
admin.approve(user)
user.show()
admin2 = AdminUser('petr', 'mail@petr.com')
admin2.approve(admin)
admin.show()