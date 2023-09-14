from monday import get_real_floor

def test_get_real_floor_with_1():
    assert get_real_floor(1) == 0


def test_get_real_floor_with_5():
    assert get_real_floor(5) == 4


def test_get_real_floor_with_15():
    assert get_real_floor(15) == 13


def test_lower_than_13():
    assert get_real_floor(1) == 0
    assert get_real_floor(0) == 0
    assert get_real_floor(5) == 4
    assert get_real_floor(10) == 9
    assert get_real_floor(12) == 11


def test_greater_than_13():
    assert get_real_floor(14) == 12
    assert get_real_floor(15) == 13
    assert get_real_floor(37) == 35
    assert get_real_floor(200) == 198


def test_basement():
    assert get_real_floor(-2) == -2
    assert get_real_floor(-5) == -5


def test_basic_test_cases():
    assert get_real_floor(1) == 0
    assert get_real_floor(5) == 4
    assert get_real_floor(15) == 13
