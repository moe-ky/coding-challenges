from challenge_01 import lookup_price, PRICE_LIST

def test_lookup_price():
    assert lookup_price(PRICE_LIST, "apple") == 0.80
    assert lookup_price(PRICE_LIST, "eggs") is None
    assert lookup_price({}, "apple") is None
