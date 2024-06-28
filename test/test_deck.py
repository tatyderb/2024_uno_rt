from scr.card import Card
from scr.deck import Deck

card_list = [Card('blue', 2), Card('red', 7), Card('yellow', 4)]

def test_create():
    deck = Deck(cards=card_list)
    assert deck.cards == card_list


def test_repr():
    deck = Deck(cards=card_list)
    assert repr(deck) == 'b2 r7 y4'


def test_load():
    deck = Deck.load('b2 r7 y4')
    # assert repr(deck) == 'b2 r7 y4'
    assert deck.cards == card_list


