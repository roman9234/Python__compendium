import datetime
import random
import threading
import time


class DeliveryService:
    def __init__(self):
        self.working_courier = threading.Semaphore(value=2)

    def deliver_package(self, package_number):
        print(f"Заказ {package_number} зарегистрирован в системе")
        self.working_courier.acquire()
        print(f"\nЗаказ {package_number} доставляется курьером...")
        time.sleep(3)
        print(f"Заказ {package_number} доставлен. Курьер освободился")
        self.working_courier.release()

    def order_processing(self, count):
        # Формируем количество потоков по числу переданных победителей
        for package_number in range(1, count + 1):
            # Эмитируем задержку в потсуплении заказов
            time.sleep(1)
            threading.Thread(target=self.deliver_package, args=[package_number]).start()


service = DeliveryService()
service.order_processing(5)
