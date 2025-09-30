# 🛒 Cash Register Python Challenges

Welcome to the **Cash Register Python Challenge Project**!  

This repo contains a sequence of beginner-friendly Python mini-projects that gradually build up to a working **cash register CLI program**. Each challenge is self-contained, and by completing them in order, you’ll practice core Python skills like variables, loops, functions, conditionals, error handling, and formatting.

---

## 📚 How It Works

- The project is divided into **challenge files** (e.g., `challenge_01.py`, `challenge_02.py`, …) in respective challenge folders.  
- Each challenge has:
  - A **starter scaffold** for the function(s) you need to implement.
  - A matching **test file** (e.g., `test_challenge_01.py`) that checks your work.  
- You complete the challenge by filling in the missing code.  
- Run the tests to see if your solution passes.  

Work through the challenges **in order** – each one builds on skills from the previous one.

At the end, you’ll put everything together into a **menu-driven CLI program** that acts as a simple cash register.

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/moe-ky/coding-challenges.git
cd python-challenges
```

### 2. Create and activate a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows PowerShell
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

> Requirements are minimal: `pytest` for testing. (No third-party libraries are used in the challenges themselves.)

---

## ▶️ Running the Tests

To check your solution for **Challenge 1**:
```bash
pytest test_challenge_01.py
```

To run **all tests** at once:
```bash
pytest
```

If all tests pass ✅, your challenge is complete!  

---

## 🚦 Challenge Structure

- **`challenge_01.py`** → Starter code for Challenge 1  
- **`test_challenge_01.py`** → Tests for Challenge 1  
- Repeat for challenges 2–10  
- **`final_integration.py`** → Where you’ll build the full CLI cash register  

---

## 🌟 Participation

- Fork this repo  
- Complete challenges in order  
- Run the tests to verify  
- (Optional) Share your solutions via pull request or in the discussions tab!  

---

## 📌 Tips

- Keep your functions **small and clear** – one task per function.  
- Follow the **rounding rules**: always round monetary values to 2 decimal places with `round(x, 2)`.  
- Don’t panic if tests fail – use them as a hint to refine your code.  
- Each file includes comments, hints, and example usage.  

---

## 🎯 Goal

By the end of this project, you’ll have:
- Practiced **dicts, lists, tuples, loops, functions, conditionals**  
- Written robust **input validation**  
- Implemented **discounts, promos, tax**  
- Built and tested a **receipt generator**  
- Assembled a working **menu-driven CLI cash register**  

---
