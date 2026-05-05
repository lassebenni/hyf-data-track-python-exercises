# HYF Data Track — Week 2 Practice Exercises

Five small exercises that consolidate Week 2 (configuration & secrets, dataclasses, separation of concerns, pytest, refactoring). Work through them in order: each one builds on patterns introduced in earlier chapters.

## Layout

Each exercise lives in its own subfolder so you can open a single Codespace and switch between them.

| Folder | Topic | Concepts |
|---|---|---|
| [`exercise_1/`](exercise_1/) | Move Secrets to .env | `python-dotenv`, `os.environ`, `config.py` |
| [`exercise_2/`](exercise_2/) | Model Data with a Dataclass | `@dataclass`, `__post_init__` validation, methods |
| [`exercise_3/`](exercise_3/) | Separate I/O from Logic | Pure functions, dependency injection, orchestration |
| [`exercise_4/`](exercise_4/) | Write Tests with Pytest | `pytest`, fixtures, parametrize |
| [`exercise_5/`](exercise_5/) | Refactor a "god function" | Combine all five concepts on one messy script |

## Two ways to run

### A. Codespace (zero setup, runs in browser)

The Week 2 Practice chapter links into the right folder via:

```
https://github.com/codespaces/new/lassebenni/hyf-data-track-python-exercises?ref=w2&folder=exercise_N
```

Inside the Codespace, all five exercises are available. The shared `.devcontainer/` at the repo root sets up Python 3.11 + the VS Code Python extensions for every folder.

### B. Local clone (use your own VS Code)

```bash
git clone -b w2 https://github.com/lassebenni/hyf-data-track-python-exercises.git
cd hyf-data-track-python-exercises
code .
```

Then open whichever exercise folder you want. Each exercise that needs extra packages ships its own `requirements.txt`; install with `pip install -r requirements.txt` from inside the folder.

## Reference solutions

When you've made an honest attempt at an exercise (or got stuck for more than 10 minutes), peek at the [`w2-solutions`](https://github.com/lassebenni/hyf-data-track-python-exercises/tree/w2-solutions) branch. Each starter file is filled in-place with the answer plus `# WHY ...:` notes explaining non-obvious choices. The original `# TODO` comments are preserved so you can read the question and the answer side-by-side.

**Read the WHY notes, not the code.** The point is the reasoning, not the syntax.
