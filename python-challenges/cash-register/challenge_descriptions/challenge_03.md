# Challenge 3 — Subtotal for a Basket

## 📝 Description
Compute the subtotal for a basket of items.  
The basket is a list of `(name, quantity)` tuples.  
Ignore unknown items and quantities ≤ 0.

## 🎯 Learning Goals
- Iterating through a list of tuples  
- Accumulating a running total  
- Reusing helper functions (`line_total`)  
- Rounding to 2 decimal places with `round(x, 2)`  

## 🔧 Function Signature
```python
def subtotal(price_list: dict[str, float], basket: list[tuple[str, int]]) -> float:
    ...
```

## 💡 Input/Output Examples
- `subtotal(PRICE_LIST, [("apple", 2), ("bread", 1)]) -> 3.10`  
- `subtotal(PRICE_LIST, [("milk", 1), ("banana", 3)]) -> 2.05`  
- `subtotal(PRICE_LIST, []) -> 0.0`  
- `subtotal(PRICE_LIST, [("unknown", 5)]) -> 0.0`  

## ✅ Acceptance Criteria
- Empty basket → `0.0`  
- Unknown items and quantities ≤ 0 → ignored  
- Correct total, rounded to 2 decimals  

## 🚀 Starter Code
```python
PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

def subtotal(price_list: dict[str, float], basket: list[tuple[str, int]]) -> float:
    total = 0.0
    # your code here
    return round(total, 2)
```

## 🕵️ Hints
- Use your `line_total` function from Challenge 2 for each item.  
- Don’t forget to round only once at the end.  

## ⚠️ Common Pitfalls
- Forgetting to skip invalid items  
- Rounding inside the loop (can cause errors)  

## 🌟 Stretch Goals
- Accept baskets as a dictionary `{name: quantity}` instead of a list of tuples.  
