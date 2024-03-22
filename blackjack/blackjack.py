""""Blackjack Game"""

from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"

MAX_POINT = 21
DEALER_HITS = 17

suits = ("♠", "♦", "♣", "♥")
ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


def shuffle(deck: list, seed: int) -> list[str]:
    """Randomises a deck of cards"""
    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)
    return copy_of_deck


def generate_deck(number_of_decks: int = 1) -> list[str]:
    """Generates a deck of cards and returns them"""
    for i in range(number_of_decks):
        return [rank + suit for suit in suits for rank in ranks]


def points_for_hand(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""

    # 2 aces and 6 cards gives 21
    aces = ("A♠", "A♦", "A♣", "A♥")
    if len(cards) > 5 or len(cards) == 2 and all(card in aces for card in cards):
        return MAX_POINT

    return sum(points_for_card(card) for card in cards)


def points_for_card(card: str) -> int:
    """Calculates the value of a card from a deck of cards"""
    if card[-1] in suits:
        rank = card[:-1]
        if rank in ("J", "Q", "K"):
            return 10
        if rank == "A":
            return 11
        if rank in ranks:
            return int(rank)
    return 0


def get_next_card_from_deck(deck: list[str]) -> str:
    """Gets the next card from the deck and returns it"""
    return deck.pop(0)


def deal_card_to_hand(deck: list[str], hand: list[str]) -> list[str]:
    """Draws a card from the deck and adds it to the hand then return the hand."""
    hand.append(get_next_card_from_deck(deck))
    return hand


def player_turn(deck: list[str], hand: list[str]) -> bool:
    """Asks the player to 'hit' or 'stick' and changes the game state based on their response"""

    print(f"Your hand is {', '.join(hand)} ({points_for_hand(hand)} points)")

    if points_for_hand(hand) >= MAX_POINT:  # Player busts or gets 21, end turn
        return False

    action = input('What do you want to do? ("hit" or "stick") ')

    if action == "hit":
        hand = deal_card_to_hand(deck, hand)
        print(f"Hitting\nYou draw {hand[-1]}")
        return True

    return False  # Stick so player's turn end


def dealer_turn(deck: list[str], hand: list[str]) -> bool:
    """The dealer takes their turn and hits if their hand points is less than 17"""

    print(f"Dealer's hand is {', '.join(hand)} ({
        points_for_hand(hand)} points)")

    if points_for_hand(hand) < DEALER_HITS:  # Dealer's hit condition
        hand = deal_card_to_hand(deck, hand)
        print(f"Dealer draws {hand[-1]}")
        return True

    return False  # Stick so dealer's turn ends


def play(seed: int) -> None:
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()
    deck = shuffle(new_deck, seed)

    # Player's turn
    player_hand = [deck.pop(0), deck.pop(0)]

    is_player_turn = True

    while is_player_turn:
        is_player_turn = player_turn(deck, player_hand)

    if points_for_hand(player_hand) > MAX_POINT:  # Player busts
        print(LOSE_MESSAGE)
        return

    # Dealer's turn
    dealer_hand = [deck.pop(0), deck.pop(0)]

    is_dealer_turn = True

    while is_dealer_turn:
        is_dealer_turn = dealer_turn(deck, dealer_hand)

    # Scoring
    if points_for_hand(dealer_hand) > MAX_POINT:  # Dealer busts
        print(WIN_MESSAGE)
        return

    # Dealer has more points than Player, you lose
    if points_for_hand(dealer_hand) > points_for_hand(player_hand):
        print(LOSE_MESSAGE)
        return

    # Player has more points than Dealer, you win
    if points_for_hand(player_hand) > points_for_hand(dealer_hand):
        print(WIN_MESSAGE)
        return

    print(DRAW_MESSAGE)


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
    play(get_seed())
