from sys import exc_info
from datetime import datetime
from market import goods, stores, storesdeco


# THESE VARS ARE NEEDED TO CHECK EXPIRED FOOD
date_future = datetime.strptime("12-12-2018", "%d-%m-%Y")
date_past = datetime.strptime("12-01-2018", "%d-%m-%Y")


def test_grocerystore_expired(modstores):
    """TESTING GROCERY MARKET FOR TRYING TO ADD EXPIRED FOOD"""
    green_1 = modstores.GroceryStore()

    apples = tuple(goods.Apple(10, date_future) for _ in range(5))
    bananas = tuple(goods.Apple(5, date_past) for _ in range(5))

    green_1.add_items(*apples)                           # ADD GOOD FOOD
    try:
        green_1.add_items(*bananas)                      # TRY ADD EXPIRED FOOD
    except ValueError:
        print("\nTEST#1 COMPLETE:\n{}".format(exc_info()))


def test_drugstore_food(modstores):
    """TESTING DRUGSTORE  FOR ADDING EXTRA FOOD"""
    belfarma_1 = modstores.DrugStore()

    apples = tuple(goods.Apple(10, date_future) for _ in range(10))

    belfarma_1.add_items(*apples[:3])                   # ADD ALLOWED COUNT FOOD
    try:
        belfarma_1.add_items(*apples[3:])               # TRY ADD EXTRA FOOD
    except ValueError:
        print("\nTEST#2 COMPLETE:\n{}".format(exc_info()))


def test_drugstore_discount(modstores):
    """TESTING DRUGSTORE FOR SETTING DISCOUNT"""
    belfarma_2 = modstores.DrugStore()

    antibiotics = tuple(goods.Antibiotic(10, date_future) for _ in range(5))

    belfarma_2.add_items(*antibiotics)

    plan_discount = 50
    for antibiotic in antibiotics:
        antibiotic.set_discount(plan_discount)                              # SET DISCOUNT 50% for all antibiotics

    price_with_discount = belfarma_2.overall_price_with_discount()
    price_no_discount = belfarma_2.overall_price_no_discount()

    real_discount = 100 * (1 - price_with_discount / price_no_discount)     # CALC REAL DISCOUNT

    print("\nTEST#3 RESULT:\nSET DISCOUNT = {}\nREAL DISCOUNT = {}".format(
        plan_discount, real_discount)
    )


if __name__ == "__main__":

    TEST_MODULES = (stores, storesdeco)

    for module in TEST_MODULES:
        print("\n--- TESTING OF THE MODULE: {} ---".format(module))
        test_grocerystore_expired(module)
        test_drugstore_food(module)
        test_drugstore_discount(module)
