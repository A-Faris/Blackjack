"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for_hand, play, get_next_card_from_deck, deal_card_to_hand
from support.testing_util import player_chooses


def test_points_for_hand():
    assert points_for_hand(['4S', '5D']) == 9


def test_points_for_hand_ten():
    assert points_for_hand(['10S', '10D']) == 20


def test_points_for_hand_letters():
    assert points_for_hand(['AS', 'KD']) == 21


def test_points_for_hand_two_aces():
    assert points_for_hand(['AH', 'AC']) == 21


def test_points_for_hand_six_cards():
    assert points_for_hand(['5C', '2S', '3D', '4C', '2C', '3S']) == 21


def test_points_for_hand_invalid_suits():
    assert points_for_hand(['5F', '6G']) == 0


def test_points_for_hand_other_point_letters():
    assert points_for_hand(['WC', 'XS']) == 0


def test_points_for_hand_other_numbers():
    assert points_for_hand(['13C', '18S']) == 0


def test_get_next_card_from_deck():
    assert get_next_card_from_deck(["2H", "3H"]) == "2H"


def test_deal_card_to_hand():
    assert deal_card_to_hand(["2H", "3H"], ["4D", "KS"]) == ["4D", "KS", "2H"]


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
    print(printed_lines)

    assert "You lose!" in printed_lines[-2]


def test_player_and_dealer_take_turns(monkeypatch, capsys):
    ...  # assert "You win!" in printed_lines


def test_same_score_draw(monkeypatch, capsys):
    player_chooses(["stick"], monkeypatch)

    play(1)

    captured_output = capsys.readouterr().out
    printed_lines = captured_output.split("\n")
    # print(printed_lines)

    assert "Draw!" in printed_lines[-2]
