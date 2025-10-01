from challenge_02 import line_total, PRICE_LIST

def test_line_total():
    assert line_total(PRICE_LIST, ("apple", 3)) == 2.40
    assert line_total(PRICE_LIST, ("eggs", 2)) == 0.0
    assert line_total(PRICE_LIST, ("milk", 0)) == 0.0
