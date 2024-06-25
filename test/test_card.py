from scr.card import Card


def test_init():
    c = Card('yellow', 8)
    assert c.color == 'yellow'
    assert c.number == 8

