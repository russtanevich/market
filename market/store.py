# market.py
from .good import Food, Tools


class Store(object):
    """Base store class"""

    _allowed_goods = ()

    def __init__(self):
        self._goods = set()                 # We will keep our goods in the set
        super(Store, self).__init__()

    def add_item(self, item):
        """ADD one item"""
        self._check_goods((item,))          # CONVERT good to tuple for maintaining of operation iter
        self._goods.add(item)               # ADD new good in our Store

    def add_items(self, *items):
        """ADD array of items"""
        self._check_goods(items)
        self._goods.update(items)

    def remove_item(self, item):
        """REMOVE one at a time"""
        self._goods.remove(item)

    def remove_items(self, *items):
        """Remove several items"""
        for item in items:
            self._goods.remove(item)

    def overall_price_no_discount(self):
        """Calculate all value of no-discount goods in the store"""
        return sum(item.price for item in self._goods if not item.discount)

    def overall_price_with_discount(self):
        """Calculate all value of discount goods in the store"""
        return sum(item.price for item in self._goods if item.discount)

    def _check_goods(self, items):
        """Check goods for validity"""
        for item in items:
            if not isinstance(item, self.__class__._allowed_goods):
                raise TypeError("Incorrect product assignment!")


class GroceryStore(Store):
    """A market where there is a food"""
    _allowed_goods = (Food,)


class HardwareGood(Store):
    """You will find no food here."""
    _allowed_goods = (Tools,)


