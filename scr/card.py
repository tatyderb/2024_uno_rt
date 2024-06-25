class Card:
    COLORS = ('red', 'green', 'blue', 'yellow')
    DCOLORS = {color[0]: color for color in COLORS}
    NUMBERS = list(range(10))

    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number

    def __repr__(self):
        letter = self.color[0]
        return f'{letter}{self.number}'

    @classmethod
    def create(cls, text: str):
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
    def all_cards():
        """Возвращает все карты."""
        pass
