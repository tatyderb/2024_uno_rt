from scr.hand import Hand


def test_hand_zero():
    h = Hand()
    assert h.cards == []
