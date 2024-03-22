# pylint: skip-file

from blackjack import generate_deck, points_for_hand, play
"""File for tests written by us - the coaches"""

from support.testing_util import player_chooses

"""
Testing Generate Deck
"""


def test_generate_deck():
    completeDeck = [
        'A♠',
        '2♠',
        '3♠',
        '4♠',
        '5♠',
        '6♠',
        '7♠',
        '8♠',
        '9♠',
        '10♠',
        'J♠',
        'Q♠',
        'K♠',
        'A♦',
        '2♦',
        '3♦',
        '4♦',
        '5♦',
        '6♦',
        '7♦',
        '8♦',
        '9♦',
        '10♦',
        'J♦',
        'Q♦',
        'K♦',
        'A♣',
        '2♣',
        '3♣',
        '4♣',
        '5♣',
        '6♣',
        '7♣',
        '8♣',
        '9♣',
        '10♣',
        'J♣',
        'Q♣',
        'K♣',
        'A♥',
        '2♥',
        '3♥',
        '4♥',
        '5♥',
        '6♥',
        '7♥',
        '8♥',
        '9♥',
        '10♥',
        'J♥',
        'Q♥',
        'K♥'
    ]

    assert generate_deck() == completeDeck


"""
Testing points_for_hand
"""


def test_points_for_empty():
    """points_for_hand() calculates the correct amount of points when no cards are present"""

    assert points_for_hand([]) == 0


def test_points_for_two_cards():
    """points_for_hand() calculates the correct amount of points when only number cards are used"""

    assert points_for_hand(['7♥', '2♦']) == 9


def test_points_five_cards():
    """points_for_hand() calculates the correct amount of points when only number and face cards are used"""

    assert points_for_hand(['3♦', 'J♣', 'Q♥', '2♥', 'A♣']) == 36


def test_points_two_aces():
    """points_for_hand() calculates the correct amount of points when there are only two aces"""

    assert points_for_hand(['A♦', 'A♣']) == 21


def test_points_two_aces_plus_one():
    """points_for_hand() calculates the correct amount of points when there are two aces and another card"""

    assert points_for_hand(['2♦', 'A♦', 'A♣']) == 24


"""
Testing gameplay
"""


def test_player_turn_output_hitting(monkeypatch, capsys):
    """player_turn(): choosing to hit outputs a "Hitting" message"""

    # The choices that a player will make during the game
    player_chooses(["hit", "stick"], monkeypatch)

    # Start our game with the given seed
    # All printed lines will be stored inside captured_output in a single string
    play(389813913)

    # Split the messages received into a list of individual lines
    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    # Check that the word Hitting is in the list
    assert "Hitting" in printed_lines


def test_player_choosing_hit_updates_hand(monkeypatch, capsys):
    """player_turn(): choosing to hit shows an updated hand"""

    player_chooses(["hit", "stick"], monkeypatch)

    play(389813913)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    printed_lines = list(
        filter(lambda m: (m.startswith('Your hand is')), printed_lines))

    assert printed_lines[1] != None
    assert "Your hand is 9♠, K♠, 9♥" in printed_lines[1]


def test_player_choosing_hit_updates_points(monkeypatch, capsys):
    """player_turn(): choosing to hit shows an updated point total"""

    player_chooses(["hit", "stick"], monkeypatch)

    play(313131)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    print(printed_lines)
    printed_lines = list(
        filter(lambda m: (m.startswith('Your hand is')), printed_lines))

    assert printed_lines[1] != None
    assert "(14 points)" in printed_lines[1]


def test_player_hitting_and_busting_lose(monkeypatch, capsys):
    """player_turn(): hitting and busting displays a 'you lose' message"""

    player_chooses(["hit"], monkeypatch)

    play(seed=1595870164262)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")

    assert "You lose!" in printed_lines
