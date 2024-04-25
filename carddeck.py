import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):  # instance method
        random.shuffle(self._cards)  # shuffle the cards

    def draw(self):
        return self._cards.pop()  # remove one card and return it

if __name__ == "__main__":
    c1 = CardDeck()
    c2 = CardDeck()
    print(f"{c1.cards = }")
    c1.shuffle()
    print(f"{c1.cards = }")
    
    for _ in range(8):
        card = c1.draw()
        print(f"{card = }")
        