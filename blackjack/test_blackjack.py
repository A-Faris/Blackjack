from blackjack import generate_deck, points_for, play
from support.testing_util import player_chooses, clean_up, capture_print_lines, take_player_turn


def test_generate_deck():
    completeDeck = [
        'AS',
        '2S',
        '3S',
        '4S',
        '5S',
        '6S',
        '7S',
        '8S',
        '9S',
        '10S',
        'JS',
        'QS',
        'KS',
        'AD',
        '2D',
        '3D',
        '4D',
        '5D',
        '6D',
        '7D',
        '8D',
        '9D',
        '10D',
        'JD',
        'QD',
        'KD',
        'AC',
        '2C',
        '3C',
        '4C',
        '5C',
        '6C',
        '7C',
        '8C',
        '9C',
        '10C',
        'JC',
        'QC',
        'KC',
        'AH',
        '2H',
        '3H',
        '4H',
        '5H',
        '6H',
        '7H',
        '8H',
        '9H',
        '10H',
        'JH',
        'QH',
        'KH'
    ]

    assert generate_deck() == completeDeck


def test_points_for_empty():
    '''pointsFor() calculates the correct amount of points when no cards are present'''

    assert points_for([]) == 0


def test_points_for_two_cards():
    ''''pointsFor() calculates the correct amount of points when only number cards are used'''

    assert points_for(['7H', '2D']) == 9


def test_points_five_cards():
    '''pointsFor() calculates the correct amount of points when only number and face cards are used'''

    assert points_for(['3D', 'JC', 'QH', '2H', 'AC']) == 36


def test_points_two_aces():
    '''pointsFor() calculates the correct amount of points when there are only two aces'''

    assert points_for(['AD', 'AC']) == 21


def test_points_two_aces_plus_one():
    '''pointsFor() calculates the correct amount of points when there are two aces and another card'''

    assert points_for(['2D', 'AD', 'AC']) == 24


def test_player_turn_output_hitting(monkeypatch):
    '''playerTurn(): choosing to hit outputs a "Hitting" message'''

    player_chooses(["hit", "stick"], monkeypatch)

    captured_output = capture_print_lines()

    take_player_turn(3131)

    printed_lines = captured_output.getvalue().split("\n")

    assert "Hitting" in printed_lines

    clean_up()


def test_player_choosing_hit_updates_hand(monkeypatch):
    '''playerTurn(): choosing to hit shows an updated hand'''

    player_chooses(["hit", "stick"], monkeypatch)

    captured_output = capture_print_lines()

    take_player_turn()

    printed_lines = captured_output.getvalue().split("\n")
    printed_lines = list(
        filter(lambda m: (m.startswith('Your hand is')), printed_lines))

    assert printed_lines[1] != None
    assert "Your hand is AS, 2S, 3S" in printed_lines[1]

    clean_up()


def test_player_choosing_hit_updates_points(monkeypatch):
    '''playerTurn(): choosing to hit shows an updated point total'''

    player_chooses(["hit", "stick"], monkeypatch)

    captured_output = capture_print_lines()

    take_player_turn()

    printed_lines = captured_output.getvalue().split("\n")
    printed_lines = list(
        filter(lambda m: (m.startswith('Your hand is')), printed_lines))

    assert printed_lines[1] != None
    assert "(16 points)" in printed_lines[1]

    clean_up()


def test_player_choosing_hit_updates_points(monkeypatch):
    '''playerTurn(): hitting and busting displays a 'you lose' message'''

    player_chooses(["hit"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed=1595870164262)

    printed_lines = captured_output.getvalue().split("\n")

    assert "You lose!" in printed_lines

    clean_up()
