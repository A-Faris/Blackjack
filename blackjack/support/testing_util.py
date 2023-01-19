import sys
from io import StringIO
from blackjack import generate_deck, player_turn, shuffle


def player_chooses(choices, monkeypatch):
    answers = iter(choices)
    monkeypatch.setattr('builtins.input', lambda name: next(answers))


def reset_test_suite():
    sys.stdout = sys.__stdout__


def capture_print_lines():
    captured_output = StringIO()
    sys.stdout = captured_output
    return captured_output
