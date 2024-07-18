# pylint: skip-file

from blackjack import generate_deck, points_for_hand, play, get_next_card_from_deck, deal_card_to_hand
from testing_util import player_chooses


def test_points_for_hand():
    assert points_for_hand(['4♠', '5♦']) == 9


def test_points_for_hand_ten():
    assert points_for_hand(['10♠', '10♦']) == 20


def test_points_for_hand_letters():
    assert points_for_hand(['A♠', 'K♦']) == 21


def test_points_for_hand_two_aces():
    assert points_for_hand(['A♥', 'A♣']) == 21


def test_points_for_hand_six_cards():
    assert points_for_hand(['5♣', '2♠', '3♦', '4♣', '2♣', '3♠']) == 21


def test_points_for_hand_invalid_suits():
    assert points_for_hand(['5F', '6G']) == 0


def test_points_for_hand_other_point_letters():
    assert points_for_hand(['W♣', 'X♠']) == 0


def test_points_for_hand_other_numbers():
    assert points_for_hand(['13♣', '18♠']) == 0


def test_get_next_card_from_deck():
    assert get_next_card_from_deck(["2♥", "3♥"]) == "2♥"


def test_deal_card_to_hand():
    assert deal_card_to_hand(["2♥", "3♥"], ["4♦", "K♠"]) == ["4♦", "K♠", "2♥"]


def test_dealer_loses_when_bust(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(3)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    # print(printed_lines)

    assert "You win!" in printed_lines[-2]


def test_player_wins_with_higher_score(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(10)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    # print(printed_lines)

    assert "You win!" in printed_lines[-2]


def test_player_loses_with_lower_score(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(2)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    # print(printed_lines)

    assert "You lose!" in printed_lines[-2]


def test_player_and_dealer_take_turns(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(1)

    captured_output = capsys.readouterr().out
    # print(captured_output)

    assert "Your hand is" and "Dealer's hand is" in captured_output


def test_same_score_draw(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(1)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    # print(printed_lines)

    assert "Draw!" in printed_lines[-2]


def test_dealer_hits_below_seventeen(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(3)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    # print(printed_lines)

    for i in range(len(printed_lines)):
        # print(i, printed_lines[i], printed_lines[i][-10:-8])
        if "Dealer's hand" in printed_lines[i] and int(printed_lines[i][-10:-8]) < 17:
            assert "Dealer draws" in printed_lines[i+1]


"""
Testing Generate Deck
"""


def test_generate_deck():
    completeDeck = [
        'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
        'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
        'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',
        'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥'
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
