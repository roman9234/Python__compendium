# Как Flask поможет при реализации REST API

# Flask - это фреймворк для создания backend-API


# Создание сервера
from flask import Flask, request

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5000)


# контроллер - это функция с декаратором @app.route

@app.route('/hello-world')
def hello_world():
    return 'Hello World'


# Для REST API мы должны иметь возможность передавать параметры внутрь FLASK-приложения
# ---- одна из возможностей - URL параметры

@app.route('/hello/<name>')
def hello_by_name(name: str):
    return f'Hello {name}'


# здесь мы прямо в URL пишем, что параметр _id должен быть целочисленным
@app.route('/blog/<int:_id>')
def show_blog(_id: int):
    return f'Blog Number {_id}'


# здесь мы прямо в URL пишем, что параметр degrees должен быть типа float
@app.route('/temperature/<float:degrees>')
def temperature(degrees: float):
    return f'You temperature is {degrees}'


# path - тип пути со слешами
@app.route('/proxy/<path:route>')
def proxy(route: str):
    return f'Let\'s proxy to: {route}'


# ---- объявление разных HTTP - методов для контроллеров
# через параметры:

@app.route('/request', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return 'This is POST'
    else:
        return 'This is GET'


# через декараторы:

@app.get('/get-request')
def get():
    return 'This is GET'


@app.post('/post-request')
def post():
    return 'This is POST'


@app.delete('/post-request')
def delete():
    return 'This is DELETE'


@app.patch('/patch-request')
def patch():
    return 'This is PATCH'


# GET параметры:
# GET - запросы по формату HTTP не имеют права иметь body

@app.get('/order')
def order():
    limit = request.args.get('limit')
    page = request.args.get('page')
    return f'Getting orders from page {page} with limit {limit}'


# Формы (сейчас используются редко)
# Если на сайте есть форма ввода
#   content-type только multipart / form-data

@app.post('/login')
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    # логика аутентификации
    return 'ok'


# ---- Response ----

# Если в ответе dictionary, Flask сам сериализует ответ в JSON
# по умолчанию возвращается 200 код ответа
@app.get("/me")
def get_me():
    return {
        "username": "Jon Show",
    }

# Если кхотим выбрать код ответа, используем кортеж
# 1 значение ответ, 2 значение код
# Строка вернётся просто как строка
@app.get("/user")
def get_user():
    return "Forbidden", 403



































