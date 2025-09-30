Challenge 1 — Look Up a Unit Price
Description

Write a function to safely look up the price of an item by name in a price list dictionary.

Learning goals:
    - Read from a dictionary
    - Return a default when a key is missing

Function signature
def lookup_price(price_list: dict[str, float], item: str) -> float | None:
    ...

PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

Input/Output examples:

    - lookup_price(PRICE_LIST, "apple") -> 0.80
    - lookup_price(PRICE_LIST, "eggs") -> None
    - lookup_price({}, "apple") -> None

Acceptance criteria:

    - Returns the float price if the item exists
    - Returns None if item is unknown (no crashes)
    - Does not modify price_list
