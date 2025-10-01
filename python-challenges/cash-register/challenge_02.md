# Challenge 2 — Line Total for One Item

## 📝 Description
Compute the total cost for a single line item `(name, quantity)`. Ignore unknown items and quantities ≤ 0.

## 🎯 Learning Goals
- Tuple unpacking  
- Guard clauses  
- Rounding to 2 decimal places with `round(x, 2)`  

## 🔧 Function Signature
```python
def line_total(price_list: dict[str, float], item: tuple[str, int]) -> float:
    ...
```

## 💡 Input/Output Examples
- `line_total(PRICE_LIST, ("apple", 3)) -> 2.40`  
- `line_total(PRICE_LIST, ("eggs", 2)) -> 0.0` (unknown)  
- `line_total(PRICE_LIST, ("milk", 0)) -> 0.0` (non-positive qty)  

## ✅ Acceptance Criteria
- Unknown items or qty ≤ 0 → return `0.0`  
- Uses `round(total, 2)`  
- Does not throw exceptions for unknown items  

## 🚀 Starter Code
```python
PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

def line_total(price_list: dict[str, float], item: tuple[str, int]) -> float:
    name, qty = item
    # your code here
    return 0.0  # replace
```

## 🕵️ Hints
- Reuse `lookup_price` from Challenge 1.  

## ⚠️ Common Pitfalls
- Forgetting to multiply by quantity  
- Rounding the unit price instead of the final total  

## 🌟 Stretch Goals
- Support floats for quantity (e.g., weighted produce)  
