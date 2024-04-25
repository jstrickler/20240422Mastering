from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in "1", "2":
            name = f"JOKER{joker_number}"
            joker = Card(name, name)
            self._cards.append(joker)

if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(j1.draw())
    print(f"{j1.cards = }")
    