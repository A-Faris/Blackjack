class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank.upper()
        self.suit = suit.upper()

    def to_string(self) -> str:
        """Returns the correct string to represent the hand"""
        return self.rank + self.suit

    @property
    def points(self) -> int:
        """Gets the correct number of points for a card"""
        if self.rank == "A":
            return 11
        if self.rank in ("J", "Q", "K"):
            return 10
        return int(self.rank)


class Hand:
    def __init__(self, cards: list) -> None:
        all_cards = all(isinstance(card, Card) for card in cards)

        if not all_cards:
            raise Exception('A Hand can only contain Cards')

        self.cards = cards

    @property
    def points(self) -> int:
        """Calculates the points for a hand of cards"""

        if len(self.cards) > 5 or len(self.cards) == 2 and all(card.rank == "A" for card in self.cards):
            return 21

        return sum(card.points for card in self.cards)


class Deck:
    suits = ("S", "D", "C", "H")
    ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self) -> None:
        # TODO Complete this method so the deck contains all the correct cards
        self.cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def draw(self) -> Card:
        """Removes and returns the top card from the deck"""
        return self.cards.pop(0)

    def shuffle(self) -> None:
        """Shuffles the cards in this deck"""
        print(self.cards)
