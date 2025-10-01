"""
Please look at challenge_01.md for the full description of this challenge.
"""

PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

def lookup_price(price_list: dict[str, float], item: str) -> float:
    return price_list.get(item, None)
