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



