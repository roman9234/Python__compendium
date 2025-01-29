from flask import Flask, request

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5000)


# Сериализация - это процесс превращения объекта в строку определённого формата
# Десериализция - обратный процесс превращения строки в объект

# Основные форматы:
# JSON
# QueryString
# XML

# Изначально фласт способен преобразовывать в JSON
@app.get('/me')
def get_me():
    name = request.json.get('name')
    return {
        "username": name,
    }


# Что если нужно обработать более сложный случай
# Можно использовать библиотеку marshmallow

# ---- Сериализация ----

from datetime import date
from marshmallow import Schema, fields


# наследуем схемы от класса Schema из модуля
class ProductSchema(Schema):
    # присваем полю name значения fields.str()
    #   показывая что именем должна быть строка
    name = fields.Str()


class OrderSchema(Schema):
    deliver_at = fields.Date()
    # nested - вызываем чтобы marshmallow работал с этим полем по вложенной схеме
    # many=True то есть работа не с одним объектом, а с массивом
    products = fields.Nested(ProductSchema(many=True))


book = dict(name="Book")
album = dict(products=[book], deliver_at=date(2022, 12, 17))
schema = OrderSchema()
# метод dump сериализцет в JSON
result = schema.dump(album)
print(result)


# {'products': [{'name': 'Book'}], 'deliver_at': '2022-12-17'}

# ---- Десериализация ----

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


user_data = {
    "created_at": "2014-08-11T05:26:03.869245",
    "email": "ken@yahoo.com",
    "name": "Ken",
}
schema = UserSchema()
result = schema.load(user_data)
print(result)
# дата преобразуется в DateTime instance
# {'name': 'Ken',
# 'email': 'ken@yahoo.com',
# 'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245)},

# ---- Валидация ----
# передаём в схему дополнительные параметры, чтобы указать как валидировать наши значения


from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))


in_data = {"name": "", "permission": "invalid", "age": 71}
try:
    UserSchema().load(in_data)
except ValidationError as err:
    print(err.messages)
# {'age': ['Must be greater than or equal to 18 and less than or equal to 40.'],
# 'name': ['Shorter than minimum length 1.'],
# 'permission': ['Must be one of: read, write, admin.']}

# ---- Интеграция с flask ----
# есть специальноя Flask marshmallow библиотека

from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

# Пример использования:

from your_orm import Model, Column, Integer, String, DateTime


class User(Model):
    email = Column(String)
    password = Column(String)
    date_created = Column(DateTime, auto_now_add=True)


############################
# Файл объявления схему сериализации
class UserSchema(ma.Schema):
    class Meta:
        # только эти поля будут сериазизованы в JSON !!!
        fields = ("email", "date_created")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# ---- Интеграция с Flask ----

@app.route("/api/users/")
def users():
    all_users = User.all()
    return users_schema.dump(all_users)


@app.route("/api/users/<id>")
def user_detail(id):
    user = User.get(id)
    return user_schema.dump(user)
