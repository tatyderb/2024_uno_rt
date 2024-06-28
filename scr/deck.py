import random

from scr.card import Card


class Deck:
    """Колода карт UNO."""

    def __init__(self, cards=None):
        if cards is None:
            cards = []
        # cards = cards or []
        self.cards = cards.copy()

    def __repr__(self):
        return ' '.join(map(str, self.cards))

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, text: str):
        """Из строки вида 'b2 r7 y4' возвращает колоду"""
        words = text.split()    # ['b2', 'r7', 'y4']
        cards = []
        for w in words:
            c = Card.load(w)
            cards.append(c)

        # cards = [Card.load(w) for w in words]

        deck = Deck(cards=cards)
        return deck

    def draw_card(self):
        """Берем карту из колоды (ее там больше нет), возвращаем эту карту."""
        c = self.cards.pop()
        return c

    def shuffle(self):
        """Перемешать колоду."""
        random.shuffle(self.cards)
