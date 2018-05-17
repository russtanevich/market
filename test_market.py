# -*- coding: utf-8 -*-
""" Home task for Class 11 """
from sys import exc_info
from market import good
from market import store


def _try_test(obj, err,  stmt, description, **kw):
    try:
        print("\n{} : {}".format(stmt, description))
        exec(stmt)
    except err:
        print(exc_info())


def test_good(prod):

    test_data = (
        (TypeError, "obj.price = -10", "SET NEGATIVE PRICE"),
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
    banana = good.Banana(10)
    apple = good.Apple(30)
    apple.set_discount(15)
    nail = good.Nail(50)
    axe = good.Axe(150)
    axe.set_discount(17)
    # TEST BANANA
    test_good(banana)
    # BUILD STORES
    bm = store.GroceryStore()
    bm.add_items(apple, banana)
    ml = store.HardwareGood()
    ml.add_items(nail, axe)
    # TEST BELMARKET
    test_store(bm, own=apple, alien=axe)
    # TEST MILE
    test_store(ml, own=axe, alien=apple)
    # CHECK DISCOUNT IN STORES
    print("\nBelmarket [no discount]: {}".format(bm.overall_price_no_discount()))
    print("Belmarket [discount]: {}".format(bm.overall_price_with_discount()))
    print("Mile [no discount]: {}".format(ml.overall_price_no_discount()))
    print("Mile [discount]: {}".format(ml.overall_price_with_discount()))






