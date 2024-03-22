# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for_hand, play, get_next_card_from_deck, deal_card_to_hand
from support.testing_util import player_chooses


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
