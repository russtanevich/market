# market.py
"""THE STORE MODULE WITHOUT DECORATORS"""
from datetime import datetime
from . import decorators as deco
from . import goods as gd


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
        self._check_good_type(item)
        self._check_expired(item)
        self._check_allowed_num(item)
        self._set_part_discount(item)
        self._goods.add(item)               # ADD new good in our Store

    def add_items(self, *items, **kwargs):
        """ADD array of items to the store."""
        count = kwargs.get("count")
        for item in items[:count]:
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

    def _check_expired(self, item):
        pass

    def _check_allowed_num(self, item):
        pass

    def _set_part_discount(self, item):
        pass

    def __str__(self):
        return "[{} #{}]".format(self.__class__.__name__, id(self))


class GroceryStore(Store):
    """A market where there is a food"""
    _allowed_goods = (gd.Food,)

    def _check_expired(self, item):
        """ACCORDING TO THE TASK WE NEED CHECK EXPIRED GOOD IN GloceryStores"""
        date_today = datetime.now()
        date_expired = item.date_expired
        # IF GOOD IS EXPIRED
        if date_today > date_expired:
            raise ValueError("{} is expired in {}. Today: {}".format(
                item, date_expired, date_today
            ))


class HardwareStore(Store):
    """You will find no food here."""
    _allowed_goods = (gd.Tool,)


class DrugStore(Store):
    """Drugs, Food, Cosmetics are here"""
    _allowed_goods = (gd.Drug, gd.Food, gd.Cosmetic)
    _constraint_positions = {gd.Food: 3}

    def _check_allowed_num(self, item):
        constraint_item = (set(type(item).mro()) & set(self.constraint_positions))
        if constraint_item:
            # IT WILL BE ONLY ONE
            constraint_item = constraint_item.pop()
            max_quantity = self.constraint_positions[constraint_item]
            # CALC CURRENT QUANTITY OF CONSTRAINT POSITIONS STORE
            current_quantity = len(
                tuple(item for item in self.goods
                      if (constraint_item in type(item).mro()))
            )
            if current_quantity >= max_quantity:
                raise ValueError("{} in {} is enough! Maximum {}. Current: {}".format(
                    constraint_item, self, max_quantity, current_quantity)
                )

    def _set_part_discount(self, item):
        """Here we use deco to half our discount"""
        item.set_discount = deco.half_discount(item.set_discount)




