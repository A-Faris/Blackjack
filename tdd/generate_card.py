"""This file is used to generate a card for the blackjack game"""

suits = ("H", "D", "C", "S")
numbers = ("1", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "J", "Q", "K", "A")


def generate_card(suit: str, number: str) -> str:
    """Generates a card based on the suit and number. (e.g. 8J) Should return an "Error" message if the suit or number is invalid."""
    if suit in suits and number in numbers:
        return number + suit
    return "Error"


def get_score(card: str) -> int:
    """Gets the score of the card (e.g. 8J returns 8). Return 0 if the card is invalid"""
    if len(card) == 2:
        if card[0] in numbers and card[-1] in suits:
            return card[0]
    return 0
