""" The utils module for market lib """
from __future__ import division

import functools

from datetime import datetime


def check_expired(func):
    """THE DECO FOR <ADD_ITEM> method for checking expired item """
    @functools.wraps(func)
    def inner(store, item):
        date_today = datetime.now()
        date_expired = item.date_expired
        # IF GOOD IS EXPIRED
        if date_today > date_expired:
            raise ValueError("{} is expired in {}. Today: {}".format(
                item, date_expired, date_today
            ))
        func(store, item)
    return inner


def check_allowed_num(func):
    """ THE DECO FOR <ADD_ITEM> method for checking allowed quantity of constraint goods """
    @functools.wraps(func)
    def inner(store, item):
        # IS THERE constraint position in MRO?
        constraint_item = (set(type(item).mro()) & set(store.constraint_positions))
        if constraint_item:
            # IT WILL BE ONLY ONE
            constraint_item = constraint_item.pop()
            max_quantity = store.constraint_positions[constraint_item]
            # CALC CURRENT QUANTITY OF CONSTRAINT POSITIONS STORE
            current_quantity = len(
                tuple(item for item in store.goods
                      if (constraint_item in type(item).mro()))
            )
            if current_quantity >= max_quantity:
                raise ValueError("{} in {} is enough! Maximum {}. Current: {}".format(
                    constraint_item, store, max_quantity, current_quantity)
                )

        func(store, item)

    return inner


def set_half_discount(func):
    """CHANGE METHOD <SET DISCOUNT> IN OUR ITEM"""
    @functools.wraps(func)
    def inner(store, item):
        item.set_discount = half_discount(item.set_discount)
        func(store, item)
    return inner


def half_discount(func):
    """THE DECO which returns only half of value"""
    @functools.wraps(func)
    def inner(discount):
        func(discount/2)
    return inner
