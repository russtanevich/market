# -*- coding: utf-8 -*-
""" Home task for Class 11 """
from datetime import datetime
from sys import exc_info
from market import goods
from market import stores


def _try_test(obj, err,  stmt, description, **kw):
    try:
        print("\n{} : {}".format(stmt, description))
        exec(stmt)
    except err:
        print(exc_info())


def test_good(prod):

    test_data = (
        (ValueError, "obj.price = -10", "SET NEGATIVE PRICE"),
        (TypeError, "obj.discount = 'abc'", "SET WRONG DISCOUNT"),
        (BaseException, "obj.freeze_price(True)", "FREEZE PRICE"),
        (AttributeError, "obj.price = 10", "SET FREEZED PRICE"),
        (AttributeError, "obj.discount = -10", "SET FREEZED PRICE")
    )
    for test_case in test_data:
        _try_test(prod, *test_case)


def test_store(store_, own, alien):

    try:
        print("\nWRONG ITEM!")
        store_.add_item(alien)
    except TypeError:
        print(exc_info())

    try:
        print("\nOWN AND ALIEN ITEMS")
        store_.add_items(own, alien)
    except TypeError:
        print(exc_info())


if __name__ == "__main__":

    # Create GOODS
    dd = datetime.strptime("12-12-2018", "%d-%m-%Y")
    banana = goods.Banana(10, dd)
    apple = goods.Apple(30, dd)
    apple.set_discount(15)

    nail = goods.Nail(50, dd)
    axe = goods.Axe(150, dd)
    axe.set_discount(17)

    # BUILD STORES
    belmarket = stores.GroceryStore()
    belmarket.add_items(apple, banana)

    apt = stores.DrugStore()
    for i in range(5):
        apt.add_items(apple, banana)

    mile = stores.HardwareStore()
    mile.add_items(nail, axe)

    # CHECK DISCOUNT IN STORES
    print("\nBelmarket [no discount]: {}".format(belmarket.overall_price_no_discount()))
    print("Belmarket [discount]: {}".format(belmarket.overall_price_with_discount()))
    belmarket.remove_item(apple)
    print("Belmarket [discount] (removed apple): {}".format(belmarket.overall_price_with_discount()))
    print("Mile [no discount]: {}".format(mile.overall_price_no_discount()))
    print("Mile [discount]: {}".format(mile.overall_price_with_discount()))

    # TEST BANANA
    test_good(banana)
    # TEST BELMARKET
    test_store(belmarket, own=apple, alien=axe)
    # TEST MILE
    test_store(mile, own=axe, alien=apple)









