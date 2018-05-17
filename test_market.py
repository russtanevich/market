# -*- coding: utf-8 -*-
""" Home task for Class 8 """
from market import good
from market import store


if __name__ == "__main__":

    apple = good.Apple(30)
    apple.set_discount(15)
    banana = good.Banana(10)

    nail = good.Nail(50)
    axe = good.Axe(150)
    axe.set_discount(17)

    bm = store.GroceryStore()
    bm.add_items(apple, banana)
    print(bm.overall_price_no_discount())
    print(bm.overall_price_with_discount())

    ml = store.HardwareGood()
    ml.add_items(nail, axe)
    print(ml.overall_price_no_discount())
    print(ml.overall_price_with_discount())





