import sys
from io import StringIO
from blackjack import generate_deck, player_turn, shuffle


def player_chooses(choices, monkeypatch):
    answers = iter(choices)
    monkeypatch.setattr('builtins.input', lambda name: next(answers))


def clean_up():
    sys.stdout = sys.__stdout__


def capture_print_lines():
    captured_output = StringIO()
    sys.stdout = captured_output
    return captured_output


def take_player_turn(seed=None):
    turn_deck = []

    if (seed == None):
        turn_deck = generate_deck()
    else:
        turn_deck = shuffle(generate_deck(), seed)

    player_hand = [turn_deck.pop(0), turn_deck.pop(0)]
    is_player_turn = True

    while (is_player_turn):
        is_player_turn = player_turn(turn_deck, player_hand)
