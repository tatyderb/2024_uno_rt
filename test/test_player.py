from scr.card import Card
from scr.hand import Hand
from scr.player import Player, AI, Human


def test_create():
    cards = Card.load('r1 b7 g3')
    hand = Hand(cards)
    p = Player(name='Alex', hand=hand)

    assert p.name == 'Alex'
    assert p.hand == hand
    assert isinstance(p.actor, AI)
