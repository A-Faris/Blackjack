import pytest
import datetime
from wednesday import get_villain_name
from random import randint

format_str = '%d/%m/%Y'  # The format


def test_get_villain_name_with_known_dates():
    assert get_villain_name(datetime.datetime.strptime(
        "1/1/2000", format_str)) == "The Evil Pickle"
    assert get_villain_name(datetime.datetime.strptime(
        "2/2/2000", format_str)) == "The Vile Hood Ornament"
    assert get_villain_name(datetime.datetime.strptime(
        "2/12/2000", format_str)) == "The Awkward Hood Ornament"


def test_get_villain_name_secret(date):
    first = ["The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing", "The Disreputable",
             "The Atrocious", "The Twirling", "The Orange", "The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat",
            "Teaspoon", "Laundry Basket"]
    m = date.month
    d = date.day % 10
    return first[m - 1] + ' ' + last[d]


def test_do_one_test():
    date = datetime.datetime.fromtimestamp(randint(0, 10e9))
    expected = test_get_villain_name_secret(date)
    actual = get_villain_name(date)
    assert actual == expected


def random_test_cases():
    for _ in range(100):
        test_do_one_test()
