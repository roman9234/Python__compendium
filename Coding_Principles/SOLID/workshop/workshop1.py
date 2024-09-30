# пример интернет-магазин

class Order:
    def __init__(self, id, products):
        pass


def get_new_id():
    pass


class OrderService:

    def __init__(self, order_repo):
        self._order_repo = order_repo

    def _apply_discount(self, order):
        # Применение скидки
        return order

    def _apply_voucher(self, order, voucher):
        # Применение скидки
        return order

    def _send_notification(self, order):
        # Отправка уведомления
        return order

    # допустим через оператора оформлять сложнее. поэтому дадим покупателям скидку за заказ через API
    # теперь у нас пояавился механизм скидочных купонов voucher - снова приходится добавлять параметр
    # а ещё при заказе с админа, добавляем флаг is_admin_order
    # а ещё в уведомлении должно быть имя оператора - плюс ещё один параметр !!
    # теперь у нас куча параметров, несколько из них дублируются (две скидки) (имя и bool для админ_order)

    def create(self, dto, should_apply_discount, voucher, is_admin_order, operator_name):
        order = Order(
            id=get_new_id(),
            products=dto["products"]
        )

        if should_apply_discount:
            order = self._apply_discount(order)

        if voucher:
            order = self._apply_voucher(order)

        if is_admin_order:
            self._send_notification(order, operator_name)
        else:
            self._send_notification(order, None)

        self._order_repo.save(order)


class APIController:
    def __init__(self, order_service: OrderService):
        self._orderService = order_service

    # API для создания заказа из корзины
    def basket_creation_endpoint(self, request):
        # validation
        return self._orderService.create(request.body["order"], should_apply_discount=True, is_admin_order=False)

    # API для создания через оператора
    def admin_creation_endpoint(self, request):
        # validation
        return self._orderService.create(request.body["order"], should_apply_discount=True, is_admin_order=True,
                                         operator_name=request.body["operator_name"])
