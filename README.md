
A collection of small, self-contained programming challenges intended for practice, learning, and interview preparation.

This repository groups challenges under the `python-challenges/` folder. Each challenge typically includes a problem description (`*.md`), a starter implementation file (`challenge_*.py`), and one or more tests (`test_*.py`) that use `pytest`.

## Getting started (high level)

1. Choose a challenge: browse the `python-challenges/` directory and open a challenge subfolder (for example, `python-challenges/cash-register/`).
2. Read the problem statement in the challenge's `*.md` file.
3. Create and activate a virtual environment (recommended) from the `python-challenges/` root:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
```

4. Install dependencies if present. There may be a top-level `python-challenges/requirements.txt` or a challenge-specific `requirements.txt`:

```bash
pip install -r python-challenges/requirements.txt
# or inside a challenge folder
pip install -r python-challenges/cash-register/requirements.txt
```

5. Run tests with `pytest` from the challenge folder:

```bash
cd python-challenges/cash-register
pytest -q
```

Tips
- Run a single test file: `pytest path/to/test_file.py`.
- Run tests that match a pattern: `pytest -k "pattern"`.
- If imports fail in tests, ensure you're running from the challenge folder or add the parent folder to `PYTHONPATH`.

## Where to find more details

See `python-challenges/README.md` for a more detailed guide: style notes, contribution guidance, troubleshooting, and expectations for solutions.

Happy coding — open an issue or PR if you'd like changes to challenge wording or to add new problems!

