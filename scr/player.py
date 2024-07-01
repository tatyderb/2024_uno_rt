from scr.hand import Hand


class Human:
    """Взаимодествие с человеком."""
    pass

class AI:
    """Решения принимает бот"""
    pass

class Player:
    def __init__(self, name: str, hand: Hand = None, is_human: bool=False):
        self.name = name
        self.hand = hand or Hand()
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def to_dict(self):
        return {
            'name': self.name,
            'hand': self.hand.save(),
            'is_human': isinstance(self.actor, Human)
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        :param data: = {
          "name": "Alex",
          "hand": "r3 y5 g4 g1",
          "is_human": true
        }
        :return: Player
        """
        return cls(name=data['name'], hand=Hand.load(data['hand']), is_human=data['is_human'])

    def save(self):
        return self.to_dict()

    @classmethod
    def load(cls, data: dict):
        return cls.from_dict(data)




