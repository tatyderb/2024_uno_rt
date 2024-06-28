from scr.card import Card


def test_init():
    c = Card('yellow', 8)
    assert c.color == 'yellow'
    assert c.number == 8

def test_print():
    c = Card('yellow', 8)
    assert str(c) == 'y8'

def test_create_from_str():
    c = Card.load('b5')
    assert c.color == 'blue'
    assert c.number == 5

def test_playable():
    c1 = Card('yellow', 8)
    c2 = Card('yellow', 1)
    c3 = Card('blue', 8)
    c4 = Card('yellow', 8)
    c5 = Card('green', 4)

    assert c1.playable(c2)
    assert c1.playable(c3)
    assert c1.playable(c4)
    assert not c1.playable(c5)


def test_all_cards():
    colors = ['blue', 'red']
    numbers = [2, 5, 7]
    cards = Card.all_cards(colors, numbers)
    assert str(cards) == "[b2, b5, b7, r2, r5, r7]"

