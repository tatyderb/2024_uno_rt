from scr.card import Card


class Hand:
    def __init__(self, cards=list[Card]):
        self.cards = cards or []

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

        deck = cls(cards=cards)
        return deck

    def __eq__(self, other):
        return self.cards == other.cards

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def is_empty(self):
        return not self.cards
