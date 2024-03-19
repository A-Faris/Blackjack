from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"

suits = ("S", "D", "C", "H")
numbers = ("A", "2", "3", "4", "5", "6",
           "7", "8", "9", "10", "J", "Q", "K")


def shuffle(deck: list, seed: int) -> list[str]:
    """Randomises a deck of cards"""
    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)
    return copy_of_deck


def generate_deck() -> list[str]:
    """Generates a deck of cards and returns them"""
    cards = []

    # TODO: Write your code here to generate a deck of cards
    for suit in suits:
        for number in numbers:
            cards.append(number + suit)
    return cards


def points_for_hand(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""

    # TODO: Write your code here
    if len(cards) > 5:
        return 21

    point = 0
    for card in cards:
        if len(card) < 4 and card[-1] in suits:
            point += points_for_card(card)
        else:
            return 0

    if len(cards) == 2 and cards[0][0] == "A" and cards[1][0] == "A":
        return 21

    return point


def points_for_card(card: str) -> int:
    if card[0] in ("J", "Q", "K"):
        return 10
    elif card[0] == "A":
        return 11
    elif card[0] in numbers:
        return int(card[0])
    elif card[:2] == "10":
        return 10
    else:
        return 0


def get_next_card_from_deck(deck: list[str]) -> str:
    """Gets the next card from the deck and returns it"""

    # TODO: Write your code here

    return deck[-1]


def deal_card_to_hand(deck: list[str], hand: list[str]) -> list[str]:
    """
    Draws a card from the deck and adds it to the hand then return the hand.
    """

    # TODO: Write your code here
    hand.append(deck.pop())
    return hand


def player_turn(deck: list[str], hand: list[str]) -> bool:
    """
    Asks the player for their next choice and changes the game state
    based on their response of either 'hit' or 'stick'
    """

    print(f"Your hand is {', '.join(hand)} ({points_for(hand)} points)")

    # Accept the choice from the player
    action = input('What do you want to do? ("hit" or "stick")')

    if action == "hit":

        hand = deal_card_to_hand(deck, hand)

        # TODO: Implement the rest of the players turn
        # It's still the player's turn

        return True
    elif action == "stick":

        return False  # End the player's turn
    else:
        return None


def play(seed: int) -> None:
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()
    shuffled_deck = shuffle(new_deck, seed)

    player_hand = [shuffled_deck.pop(0), shuffled_deck.pop(0)]

    is_player_turn = True

    while is_player_turn:
        is_player_turn = player_turn(shuffled_deck, player_hand)

    # TODO: Implement the Dealer's turn

    # TODO: Implement the end of the game


def get_seed() -> int:
    """
    You can safely ignore this function. It is used to accept a seed from the command line.
    For example

    python3 blackjack.py --seed 313131

    Would play the game with defined seed of 313131
    """
    parser = argparse.ArgumentParser("blackjack")
    parser.add_argument(
        "--seed", dest='seed', help="The seed that a game will be played with", type=int)
    args = parser.parse_args()
    seed = args.seed

    if seed is None:
        return time()

    return seed


if __name__ == "__main__":
    seed = get_seed()
    play(seed)
