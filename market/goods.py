from __future__ import division


class Good(object):

    def __init__(self, price, expired, discount=0):
        self._freeze = False

        assert float(price) > 0, "Price must be numeric and positive or zero!"
        assert 0 <= float(discount) <= 100, "Discount must be numeric in range 0..100"

        self._price = float(price)
        self._discount = float(discount)
        self._date_expired = expired

    @property
    def source_price(self):
        return self._price

    @property
    def price(self):
        """Get price with discount percent"""
        return self._price * (100 - self.discount) / 100

    @price.setter
    def price(self, value):
        """Check of value for validity"""
        if self.freeze:
            raise AttributeError("The price is freeze!")
        elif not isinstance(value, (int, float)):
            raise TypeError("Price must be <Integer> or <Float>")
        elif value < 0:
            raise ValueError("Price must be more then 0")
        else:
            self._price = value

    @property
    def discount(self):
        """Just return discount percent"""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Check of value for validity"""
        if self.freeze:
            raise AttributeError("The discount is freeze!")
        if not isinstance(value, (int, float)):
            raise TypeError("Discount must be <Integer> or <Float>!")
        if not (0 <= value <= 100):
            raise ValueError("Discount must be in range 0..100!")
        else:
            self._discount = value

    def set_discount(self, value):
        self.discount = value

    def reset_discount(self):
        self.discount = 0

    @property
    def date_expired(self):
        return self._date_expired

    @property
    def freeze(self):
        return self._freeze

    @freeze.setter
    def freeze(self, value):
        """Check of value for validity"""
        if isinstance(value, bool):
            self._freeze = value
        else:
            raise TypeError("freeze must be <bool> type!")

    def freeze_price(self, value):
        self.freeze = value

    def __str__(self):
        return "[{} #{}]".format(self.__class__.__name__, id(self))



class Cosmetic(Good):
    pass


class Drug(Good):
    pass


class Food(Good):
    pass


class Tool(Good):
    pass


class Clay(Cosmetic):
    pass


class Antibiotic(Drug):
    pass


class Banana(Food):
    pass


class Apple(Food):
    pass


class Nail(Tool):
    pass


class Axe(Tool):
    pass
