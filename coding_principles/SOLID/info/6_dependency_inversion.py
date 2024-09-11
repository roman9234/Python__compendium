# принцип инверсии зависимостей - Dependency Inversion

# Зависимость от абстракции, нет зависимости от конкретики

# Важно чтобы классы использовали интерфейсы,
# а не от одного единственного класса реализации




# Что даёт:

# соблюдение Open-close принципа
# можно легко менять зависимости
# высокая тестируемость кода
# высокая переиспользуемость кода




# Хороший пример:

# Класс работы с файлами, который зависит от файлового менеджера




# Плохой пример:

# Класс работы с файлами, который зависит от класса файлового менеджера для работы с файловой системой

