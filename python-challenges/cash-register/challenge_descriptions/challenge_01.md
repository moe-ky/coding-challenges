# Challenge 1 — Price Lookup

## 📝 Description
Write a function that looks up the price of a given item in a price list.  
If the item is not found, return `0.0`.

## 🎯 Learning Goals
- Accessing dictionary values  
- Using `dict.get()` safely  
- Returning default values when a key is missing  

## 🔧 Function Signature
```python
def lookup_price(price_list: dict[str, float], item: str) -> float:
    ...
```

## 💡 Input/Output Examples
- `lookup_price(PRICE_LIST, "apple") -> 0.80`  
- `lookup_price(PRICE_LIST, "bread") -> 1.50`  
- `lookup_price(PRICE_LIST, "unknown") -> 0.0`  

## ✅ Acceptance Criteria
- Returns the correct price if item exists  
- Returns `0.0` if item does not exist  
- Always returns a float  

## 🚀 Starter Code
```python
PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

def lookup_price(price_list: dict[str, float], item: str) -> float:
    # your code here
    return 0.0  # replace
```

## 🕵️ Hints
- Try using `price_list.get(item, 0.0)` to avoid KeyErrors.  

## ⚠️ Common Pitfalls
- Forgetting to return `0.0` for unknown items  
- Returning `None` instead of a float  

## 🌟 Stretch Goals
- Make the lookup case-insensitive (e.g., `"Apple"` should match `"apple"`)  
