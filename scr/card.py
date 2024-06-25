class Card:
    COLORS = ('red', 'green', 'blue', 'yellow')
    NUMBERS = list(range(10))

    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number
        