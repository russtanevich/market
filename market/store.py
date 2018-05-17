# market.py
from .good import Food, Tools


class Store(object):

    _allowed_goods = ()

    def __init__(self):
        self._goods = set()
        super(Store, self).__init__()

    def add_item(self, item):
        self._check_goods(tuple(item))          # CONVERT good to tuple for maintaining of operation iter
        self._goods.add(item)                   # ADD new good in our Store

    def add_items(self, *items, **kwargs):
        self._check_goods(items)
        self._goods.update(items)

    def remove_item(self, item):
        self._goods.remove(item)

    def remove_items(self, *items):
        for item in items:
            self._goods.remove(item)

    def overall_price_no_discount(self):
        price = 0
        for item in self._goods:
            if not item.discount:
                price += item.price
        return price

    def overall_price_with_discount(self):
        price = 0
        for item in self._goods:
            if item.discount:
                price += item.price
        return price

    def _check_goods(self, items):
        for item in items:
            if not isinstance(item, self.__class__._allowed_goods):
                raise TypeError("Incorrect product assignment!")


class GroceryStore(Store):
    _allowed_goods = (Food,)


class HardwareGood(Store):
    _allowed_goods = (Tools,)


