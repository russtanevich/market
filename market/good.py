from __future__ import division

class Good(object):

    def __init__(self, price, discount=0):
        self.freeze = False
        self.price = price
        self.discount = discount

    @property
    def price(self):
        """Get price with discount percent"""
        return self.__price * (100 - self.__discount) / 100

    @price.setter
    def price(self, value):
        """Check of value for validity"""
        if self.freeze:
            raise AttributeError("The price is freeze!")
        elif isinstance(value, (int, float)) and value > 0:
            self.__price = value
        else:
            raise TypeError("Price must be <Integer> or <Float> and more then 0")

    @property
    def discount(self):
        """Just return discount percent"""
        return self.__discount

    @discount.setter
    def discount(self, value):
        """Check of value for validity"""
        if self.freeze:
            raise AttributeError("The discount is freeze!")
        if isinstance(value, (int, float)) and (0 <= value <= 100):
            self.__discount = value
        else:
            raise TypeError("Discount must be <Integer> or <Float> and in range 0..100")

    def set_discount(self, value):
        self.discount = value

    def reset_discount(self):
        self.discount = 0

    @property
    def freeze(self):
        return self.__freeze

    @freeze.setter
    def freeze(self, value):
        """Check of value for validity"""
        if isinstance(value, bool):
            self.__freeze = value
        else:
            raise TypeError("freeze must be <bool> type!")

    def freeze_price(self, value):
        self.freeze = value


class Food(Good):
    pass


class Tools(Good):
    pass


class Banana(Food):
    pass


class Apple(Food):
    pass


class Nail(Tools):
    pass


class Axe(Tools):
    pass
