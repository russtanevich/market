# market.py
from . import goods as gd
from . import decorators as deco


class Store(object):
    """Base store class"""

    _allowed_goods = ()                     # A TUPLE OF ALLOWED GOODS
    _constraint_positions = {}              # A TABLE of GOOD and ALLOWED QUANTITY

    def __init__(self):
        self._goods = set()                 # We will keep our goods in the set

    @property
    def goods(self):
        return  self._goods

    @property
    def allowed_goods(self):
        return self._allowed_goods

    @property
    def constraint_positions(self):
        return self._constraint_positions

    def add_item(self, item):
        """ADD one item"""
        self._check_good_type(item)         # CONVERT good to tuple for maintaining of operation iter
        self._goods.add(item)               # ADD new good in our Store

    def add_items(self, *items):
        """ADD array of items"""
        for item in items:
            self.add_item(item)

    def remove_item(self, item):
        """REMOVE one at a time"""
        self._goods.remove(item)

    def remove_items(self, *items):
        """Remove several items"""
        for item in items:
            self.remove_item(item)

    def overall_price_no_discount(self):
        """Calculate all value of no-discount goods in the store"""
        return sum(item.source_price for item in self._goods)

    def overall_price_with_discount(self):
        """Calculate all value of discount goods in the store"""
        return sum(item.price for item in self._goods)

    def _check_good_type(self, item):
        """Check goods for validity"""
        if not isinstance(item, self._allowed_goods):
            raise TypeError(
                "TAKEN: {}, BUT EXPECTED: {}".format(item, self._allowed_goods)
            )


    def __str__(self):
        return "[{} #{}]".format(self.__class__.__name__, id(self))


class GroceryStore(Store):
    """A market where there is a food"""
    _allowed_goods = (gd.Food,)

    @deco.check_expired
    def add_item(self, item):
        super(GroceryStore, self).add_item(item)


class HardwareStore(Store):
    """You will find no food here."""
    _allowed_goods = (gd.Tool,)


class DrugStore(Store):
    """Drugs, Food, Cosmetics are here"""
    _allowed_goods = (gd.Drug, gd.Food, gd.Cosmetic)
    _constraint_positions = {gd.Food: 3}

    @deco.set_half_discount
    @deco.check_allowed_num
    def add_item(self, item):
        super(DrugStore, self).add_item(item)




