# https://www.youtube.com/watch?v=HIWfeIHocUc
import random
from check_time import *


"""
Сравнение циклов с генераторами
"""


USERS_BUY = [
    ("confirmed", 100),
    ("unconfirmed", 500),
    ("confirmed", 900),
]


def fill_users_list():
    global USERS_BUY
    temp = [("confirmed", random.randint(10, 200)) for user in range(1_000_000)]
    USERS_BUY += temp


@check_time
def cycle_example():
    res = 0

    for user in USERS_BUY:
        if user[0] == "confirmed":
            res += user[1]
    print(res)


@check_time
def list_example():
    balance_list = [user[1] for user in USERS_BUY if user[0] == "confirmed"]
    res = sum(balance_list)
    print(res)


@check_time
def generator_example():
    balance_list = (user[1] for user in USERS_BUY if user[0] == "confirmed")
    res = sum(balance_list)
    print(res)


if __name__ == "__main__":
    fill_users_list()

    cycle_example()

    list_example()

    generator_example()
