from scr.card import Card


def test_init():
    c = Card('yellow', 8)
    assert c.color == 'yellow'
    assert c.number == 8

def test_print():
    c = Card('yellow', 8)
    assert str(c) == 'y8'

def test_create_from_str():
    c = Card.create('b5')
    assert c.color == 'blue'
    assert c.number == 5

