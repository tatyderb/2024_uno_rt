from abc import ABC, abstractmethod

from scr.card import Card, CardException
from scr.hand import Hand

class PlayerInteractions(ABC):
    @abstractmethod
    def choose_card(self, hand: Hand, top: Card, card_counts: list[int]) -> Card | None:
        pass

class Human(PlayerInteractions):
    """Взаимодествие с человеком."""
    def choose_card(self, hand: Hand, top: Card, card_counts: list[int]) -> Card | None:
        '''
        Введите какую карту играем из руки: п4
        Такой карты нет в руке
        Введите какую карту играем из руки: g4
        '''
        while True:
            res = input('Введите какую карту играем из руки: ')
            try:
                card = Card.load(res)
                if card in hand.cards:
                    return card
                else:
                    print('Такой карты нет в руке')
            except CardException:
                print('Такой карты не существует')


class AI(PlayerInteractions):
    """Решения принимает бот"""
    def choose_card(self, hand: Hand, top: Card, card_counts: list[int]) -> Card | None:
        """Выбирает первую подходящую карту с руки, иначе None"""
        # random.choose
        # cards = hand.playable_cards(top) <--

        # cards = []
        # for c in hand.cards:
        #     if top.playable(c):
        #         cards.append(c)
        cards = [c for c in hand.cards if top.playable(c)]
        # if cards:                   # bool([])
        #     return None
        # else:
        #     return cards[0]
        return cards[0] if cards else None



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

    def choose_card(self, top: Card, card_counts: list[int]) -> Card | None:
        return self.actor.choose_card(self.hand, top, card_counts)


def human_choose_card():
    """Только для ручного тестирования методов!"""
    hand = Hand.load('r1 b7 g3')
    p = Player(name='Alex', hand=hand, is_human=True)
    # первую из нескольких
    top = Card('green', 7)

    print(p)
    card = p.actor.choose_card(hand=hand, top=top, card_counts=[len(p.hand.cards), 3, 4])
    print(f'resulted card={card}')


if __name__ == '__main__':
    human_choose_card()



