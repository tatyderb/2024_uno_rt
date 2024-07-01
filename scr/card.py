class Card:
    COLORS = ('red', 'green', 'blue', 'yellow')
    DCOLORS = {color[0]: color for color in COLORS}
    NUMBERS = list(range(10)) + list(range(1, 10))

    def __init__(self, color: str, number: int):
        if color in Card.DCOLORS.keys() or color in Card.DCOLORS.values():
            self.color = color
        else:
            raise ValueError(f'Unexpected color {color}')
        if number in Card.NUMBERS:
            self.number = number
        else:
            raise ValueError(f'Unexpected number {number}')

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number

    def __repr__(self):
        letter = self.color[0]
        return f'{letter}{self.number}'

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, text: str):
        """Создает карту из строки вида 'y8' и возвращает её."""
        # text = 'y8'
        letter = text[0]   # 'y'
        number = text[1]   # '8'
        color = cls.DCOLORS[letter]
        card = Card(color, int(number))
        return card

    def playable(self, other) -> bool:
        """Можно ли играть карту self на карту other."""
        return self.color == other.color or self.number == other.number

    @staticmethod
    def all_cards(colors=None, numbers=None):
        """Возвращает все карты.
        :param colors:
        :param numbers:
        """
        if colors is None:
            colors = Card.COLORS
        if numbers is None:
            numbers = Card.NUMBERS

        cards = []
        for col in colors:
            for n in numbers:
                c = Card(col, n)
                cards.append(c)

        # return [Card(col, n) for col in colors for n in numbers]
        return cards

