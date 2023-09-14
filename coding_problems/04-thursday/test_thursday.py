from thursday import best_friend
from string import ascii_lowercase as al


def test_best_friend_with_known_inputs_1():
    assert best_friend('he headed to the store', 'h', 'e') == True


def test_best_friend_with_known_inputs_2():
    assert best_friend('i found an ounce with my hound', 'o', 'u') == True


def test_best_friend_with_known_inputs_3():
    assert best_friend('those were their thorns they said', 't', 'h') == True


def test_best_friend_with_known_inputs_4():
    assert best_friend('we found your dynamite', 'd', 'y') == False


def test_best_friend_with_known_inputs_5():
    assert best_friend('look they took the cookies', 'o', 'o') == False


def test_best_friend_with_known_inputs_6():
    assert best_friend('a test', 't', 'e') == False


def test_best_friend_with_known_inputs_7():
    assert best_friend('abcdee', 'e', 'e') == False


def test_best_friend_with_known_inputs_8():
    assert best_friend('abcde', 'e', 'e') == False
