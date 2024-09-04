# Свойства хорошего кода
# Хороший код - организован таким образом, что позволяет понимать и вносить изменения в эту спецификацию с наименьшими усилиями и рисками.
# Свойства хорошего кода и подходы к его организации, таким образом, ориентированы на управление сложностью.
# Сложность кода может быть неотъемлемой – присущей предметной области или заданным техническим характеристикам – или привнесенной, побочной.
import math
from datetime import datetime
from math import cos, asin, sqrt, pi
# ---- Abstraction ----
# Abstraction (абстрактность кода) — степень приближенности кода к языку предметной области, в которой он оперирует;
# достигается при помощи выделение ключевых элементов логики кода в отдельные переиспользуемые фрагменты с целью сокрытия несущественных деталей.

# ---- До
# функция форматирует список, но она не должна отвечать за то, как мы логируем информацию.
# Это смешение бизнес-логики форматирования и логирования

from typing import List, Callable, Any, Optional, Dict


def render_items(items: List[str]) -> str:
    result = '\n'.join(
        [f'* {item}' for item in items]
    )
    print(
        f'Rendered {len(items)} items in Markdown'
    )
    return result


# После ---- (выделение функции)

def log_message(msg: str):
    print(msg)


def render_items(items: List[str]) -> str:
    result = '\n'.join(
        [f'* {item}' for item in items]
    )
    log_message(
        f'Rendered {len(items)} items in Markdown'
    )
    return result


print(render_items(["item 1", "item 2", "item 3"]))


# ---- До
# В классе смешиваются уровни абстракции - смешивается логика форматирования и логгирования

class MarkdownRenderer:
    def render_items(self, items: List[str]) -> str:
        result = '\n'.join(
            [f'* {item}' for item in items]
        )
        print(
            f'Rendered {len(items)} items in Markdown'
        )
        return result


# После ---- (выделение класса)

class ConsoleLogger:
    def log_message(self, msg: str):
        print(msg)


class MarkdownRenderer:
    logger = ConsoleLogger()

    def render_items(self, items: List[str]) -> str:
        result = '\n'.join(
            [f'* {item}' for item in items]
        )
        self.logger.log_message(
            f'Rendered {len(items)} items in Markdown'
        )
        return result


# ---- До
# Клиенский код берёт на себя часть логики логгирования. Формат логгирования должен быть скрыт

class ConsoleLogger():
    def log_message(self, msg: str):
        print(msg)


logger = ConsoleLogger()
time = datetime.now().isoformat()
logger.log_message(
    f"[ERROR][{time}] Some issue occured"
)


# После ---- (Сокрытие логики)

class LogLevel(Enum):
    INFO = "INFO"
    ERROR = "ERROR"


class ConsoleLogger():
    def log_message(
            self,
            msg: str,
            level: LogLevel
    ):
        time = datetime.now().isoformat()
        print(f"[{level.name}][{time}] {msg}")


logger = ConsoleLogger()
logger.log_message("Some issue occured", LogLevel.ERROR)


# ---- Composition ----
# Composition (компоновка кода) — подход к формированию кода из независимых и заменяемых компонентов, собранных в единую логику исполнения.
# Абстрактный код хорошо компонуем
# ---- До
# Всего один класс

class ConsoleLogger:
    def log_message(self, msg: str):
        print(msg)


# После ---- (Составили иерархию классов)

class Logger:  # описывает интерфейс
    def log_message(self, msg: str):
        pass


class ConsoleLogger(Logger):
    def log_message(self, msg: str):
        print(msg)


class NetworkLogger(Logger):
    def __init__(self, host: str, port: int):
        # self.udp_client = socket.socket(
        #     family=socket.AF_INET, type=socket.SOCK_DGRAM
        # )
        # self.address = (host, port)
        pass

    def log_message(self, msg: str):
        # self.udp_client.sendto(str.encode(msg), self.address)
        pass


logger1 = ConsoleLogger()
logger2 = NetworkLogger("127.0.0.1", 1234)
# оба класса имеют один интерфейс, поэтому используются одинаково
logger1.log_message("test")
logger2.log_message("test")


# ---- До
# Класс MarkdownRenderer использует ConsoleLogger напрямую.
# Вместо этого мы внесём его в конструктор, и за счёт этого MarkdownRenderer сможет использовать любой логгер с тем же интерфейсом


class MarkdownRenderer:
    logger = ConsoleLogger()

    def render_items(self, items: List[str]) -> str:
        result = '\n'.join(
            [f'* {item}' for item in items]
        )
        self.logger.log_message(
            f'Rendered {len(items)} items in Markdown'
        )
        return result


r = MarkdownRenderer()
print(r.render_items(["item 1", "item 2", "item 3"]))


# После ---- (dependency injection - внедрение зависимости снаружи)


class MarkdownRenderer:
    def __init__(self, logger: Logger):
        self.logger = logger

    def render_items(self, items: List[str]) -> str:
        result = '\n'.join(
            [f'* {item}' for item in items]
        )
        self.logger.log_message(
            f'Rendered {len(items)} items in Markdown'
        )
        return result


r = MarkdownRenderer(
    logger=NetworkLogger("127.0.0.1", 1234)
)
print(r.render_items(["item 1", "item 2", "item 3"]))


# ---- До
# Вместо конкретной функции log_message, render_items может вызывать любую другую, поданную как параметр

def render_items(items: List[str]) -> str:
    result = '\n'.join(
        [f'* {item}' for item in items]
    )
    log_message(
        f'Rendered {len(items)} items in Markdown'
    )
    return result


# После ---- (higher-order function)

def render_items(items: List[str], log_message_fn: Callable[[str], Any]) -> str:
    result = '\n'.join(
        [f'* {item}' for item in items]
    )
    log_message_fn(
        f'Rendered {len(items)} items in Markdown'
    )
    return result


print(render_items(["item 1", "item 2", "item 3"], log_message_fn=print))
print(render_items(["item 1", "item 2", "item 3"], log_message_fn=lambda msg: None))


# ---- Хороший код: Low coupling and High cohesion ----
# High cohesion Позволяет сконцентрировать неотъемлимую сложность внутри самих компонентов
# Low coupling даёт возможность независимо изучать и изменять компоненты кода

# ---- Coupling ----
# Coupling (внешняя связность) — факт или степень зависимости между компонентами кода.

# ---- Cohesion ----
# Cohesion (внутренняя связность, цельность) — устройство компонента кода с целью сокрытия сложности внутри его реализации.

# ---- Пример изменения кода ----

class Delivery:
    is_started: bool = False
    driver_lon: float = 0.0
    driver_lat: float = 0.0

    def __init__(
            self,
            product1: str,
            amount1: int,
            product2: str,
            amount2: str
    ):
        self.product1 = product1
        self.amount1 = amount1
        self.product2 = product2
        self.amount2 = amount2


class Driver:

    def __init__(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat

    def start_delivery(self, delivery: Delivery):
        delivery.is_started = True
        self.update_delivery(delivery)

    def update_delivery(self, delivery: Delivery):
        delivery.driver_lon = self.lon
        delivery.driver_lat = self.lat


class Customer:

    def __init__(self, address: str):
        self.address = address

    def get_delivery_status(self, delivery: Delivery) -> str:
        if delivery.is_started:
            location = geocode(self.address)
            p = math.pi / 180
            a = \
                0.5 - math.cos((location.lat - delivery.driver_lat) * p) / 2 + \
                math.cos(location.lat * p) * math.cos(delivery.driver_lat * p) * \
                (1 - math.cos((location.lon - delivery.driver_lon) * p)) / 2
            distance = 12742 * math.asin(math.sqrt(a))
            return f"Driver is {distance:.1f} km away"
        else:
            return "Delivery hasn't been started yet"

    @staticmethod
    def update_order(delivery: Delivery, product: str, amount) -> str:
        if delivery.is_started:
            return "Cannot modify started delivery"
        elif delivery.product1 == product:
            delivery.amount1 = amount
            return "Success"
        elif delivery.product2 == product:
            delivery.amount2 = amount
            return "Success"
        else:
            return "Delivery cannot contain more than 2 products"


def delivery_scenario():
    customer = Customer("Moscow, Ulitsa Pyatnitskaya, 3")
    delivery = Delivery("apples", 1, "oranges", 2)
    customer.get_delivery_status(delivery)
    # 'Delivery hasn't been started yet'
    customer.update_order(delivery, "apples", 3)
    # 'Success'
    customer.update_order(delivery, "peaches", 5)
    # 'Delivery cannot contain more than 2 products'

    driver = Driver(37.1, 55.2)
    driver.start_delivery(delivery)

    customer.get_delivery_status(delivery)
    # 'Driver is 22.0 km away'
    customer.update_order(delivery, "apples", 4)
    # 'Cannot modify started delivery'

    driver.lon = 37.2
    driver.lat = 55.3
    driver.update_delivery(delivery)

    customer.get_delivery_status(delivery)
    # 'Driver is 12.7 km away'


# Проблемы:

# Низкий уровень абстракции кода: В методе get_delivery_status смешаны логика определения статуса и расчета расстояний,
# их необходимо разделить, т.к. реализация каждой из частей независима по отношению к другой и несущественна для нее.

# Высокая связность между классами:
# ★ Customer и Driver напрямую манипулируют параметрами Delivery, и таким образом сильно зависят от его внутреннего устройства.
# ★ Часть ответственности за ограничение «не более 2 продуктов в Delivery» лежит на
# Customer.

# Низкая цельность классов:
# ★ Deliverу не содержит никакой логики, а также не имеет достаточно информации для ее реализации (например, не хранит адрес доставки).
# ★ Customer и Driver берут на себя не существенную для себя логику работы со статусом доставки.

# Неудачная компоновка: Customer не имеет информации о том, есть ли у него активная доставка, Driver – какую доставку обновить при изменении местоположения.
# Эти пробелы заполняет логика в delivery_scenario, создавая неявную зависимость работоспособности системы от деталей работы клиентского кода.

# После ---- ()

class Driver:
# теперь не отвечает за обновление координат delivery

    def __init__(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat

    def update_position(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat


class DistanceService:

    @staticmethod
    def get_distance(lon: float, lat: float, address: str) -> float:
        location = geocode(address)
        p = math.pi / 180
        a = \
            0.5 - math.cos((location.lat - lat) * p) / 2 + \
            math.cos(location.lat * p) * math.cos(lat * p) * \
            (1 - math.cos((location.lon - lon) * p)) / 2
        return 12742 * math.asin(math.sqrt(a))


class Delivery:
    # теперь реализует основную часть логики
    # теперь скрывает за интерфейсом логику проверки корректности заказа и определения статуса
    # теперь класс distance_service абстрагирует Delivery от детали работы с адресами и расстоянием


    driver: Optional[Driver] = None
    distance_service = DistanceService()

    @staticmethod
    def validate_order(order: Dict[str, int]):
        if not (0 < len(order) <= 2):
            raise ValueError("Delivery cannot contain more than 2 products")

    def __init__(self, order: Dict[str, int], address: str):
        Delivery.validate_order(order)
        self.order = order
        self.address = address

    def start(self, driver):
        self.driver = driver

    def is_started(self) -> bool:
        return self.driver is not None

    def get_status(self) -> str:
        if self.is_started():
            distance =\
            self.distance_service.get_distance(
                self.driver.lon,
                self.driver.lat,
                self.address
            )
            return f"Driver is {distance:.1f} km away"
        else:
            return "Delivery hasn't been started yet"


def update_order(self, product: str, amount: str) -> str:
    if self.is_started():
        return "Cannot modify started delivery"
    else:
        new_order = self.order.copy()
        new_order[product] = amount
        try:
            Delivery.validate_order(new_order)
        except ValueError as e:
            return str(e)
        self.order = new_order
        return "Success"


class Customer:
# теперь ничего не знает о внутреннем устройстве класса delivery
# зато теперь зависимость от delivery сделана явной
    delivery: Optional[Delivery] = None

    def __init__(self, address: str):
        self.address = address

    def order_delivery(self, order: Dict[str, int]) -> Delivery:
        self.delivery = Delivery(order, self.address)
        return self.delivery

    def get_delivery_status(self) -> str:
        if self.delivery is not None:
            return self.delivery.get_status()
        else:
            return "No delivery ordered"

    def update_order(self, product: str, amount: str) -> str:
        if self.delivery is not None:
            return self.delivery.update_order(product, amount)
        else:
            return "No delivery ordered"


# теперь сценарий проще и решже упоминает вудшмукн
def delivery_scenario_v2():
    customer = Customer("Moscow, Ulitsa Pyatnitskaya, 3")
    delivery = customer.order_delivery({"apples": 1, "oranges": 2})
    customer.get_delivery_status()
    customer.update_order("apples", 3)
    customer.update_order("peaches", 5)
    driver = Driver(37.1, 55.2)
    delivery.start(driver)
    customer.get_delivery_status()
    customer.update_order("apples", 4)
    driver.update_position(37.2, 55.3)
    customer.get_delivery_status()


# Правила сохранения хорошего кода:
# непрерывный рефакторинг
# The boy scout rule: всегда оставляйте код лучше, чем он был до вас
# Совместная работа с заказчиком - выработка понимания того, в каких случаях инвестиции в качество кода
# оправданы в долгосрочной перспективе