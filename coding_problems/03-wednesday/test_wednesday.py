import datetime
from wednesday import get_villain_name

format_str = '%d/%m/%Y'  # The format


def test_get_villain_name_with_known_dates_evil_pickle():
    assert get_villain_name(datetime.datetime.strptime(
        "1/1/2000", format_str)) == "The Evil Pickle"


def test_get_villain_name_with_known_dates_vile_hood():
    assert get_villain_name(datetime.datetime.strptime(
        "2/2/2000", format_str)) == "The Vile Hood Ornament"


def test_get_villain_name_with_known_dates_awkward_good():
    assert get_villain_name(datetime.datetime.strptime(
        "2/12/2000", format_str)) == "The Awkward Hood Ornament"
