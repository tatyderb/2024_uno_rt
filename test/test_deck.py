import random

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

def test_draw_card():
    deck = Deck(cards=card_list)
    c = deck.draw_card()
    assert str(c) == 'y4'
    assert str(deck) == 'b2 r7'

def test_shuffle():
    random.seed(7)
    deck = Deck.load('y2 y6 y9 b3 b5 b1 g4 g6 g1 g2 r0')
    deck.shuffle()
    assert str(deck) == 'y6 r0 b3 g2 g1 b5 g6 y2 g4 y9 b1'
    deck.shuffle()
    assert str(deck) == 'b3 b5 g1 y2 b1 g6 y9 r0 y6 g2 g4'
    deck.shuffle()
    assert str(deck) == 'r0 y6 g1 g4 b1 y9 g6 y2 b5 g2 b3'
    deck.shuffle()
    assert str(deck) == 'y9 b1 g6 b5 y6 g2 y2 g1 b3 g4 r0'




