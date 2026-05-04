# HYF Data Track — Week 1 Practice Exercises *(with reference solutions)*

> ⚠️ **You're on the `w1-solutions` branch.** This branch carries the same six starters as `w1` **plus** a `solution.py` next to each one. Open it AFTER you've attempted the exercises on `w1` — the whole point of the practice block is the struggle, not the answer key.
>
> If you landed here by mistake and want clean starters: switch to the [`w1` branch](https://github.com/lassebenni/hyf-data-track-python-exercises/tree/w1).

Six small exercises that consolidate Week 1 (variables, functions, type hints, logging, debugging, file I/O, CLI). Pick the ones that match what felt shaky on a first read of the chapter; you can do them in any order.

## Layout

Each exercise lives in its own subfolder. Both the starter and the reference solution live side-by-side; you choose when to open `solution.py`.

| Folder | Topic | Concepts | Files |
|---|---|---|---|
| [`exercise_1/`](exercise_1/) | The Temperature Logger | Variables, functions, type hints, logging | `exercise.py` + `solution.py` |
| [`exercise_2/`](exercise_2/) | The Data Cleaner | Lists, loops, conditionals, debugging | `exercise_2.py` + `solution.py` |
| [`exercise_3/`](exercise_3/) | The Precision Trap | Floating-point math, debugger usage | `exercise.py` + `solution.py` |
| [`exercise_4/`](exercise_4/) | Grade Processor | Dictionaries, type hints, logging, branching | `exercise.py` + `solution.py` |
| [`exercise_5/`](exercise_5/) | The File Ingestor | File I/O, context managers, strings | `assignment_6.py` + `solution.py` |
| [`exercise_6/`](exercise_6/) | The Pipeline CLI | argparse, logging levels, pathlib | `exercise_6.py` + `solution.py` + `data/` |

## How to use this branch

1. **Attempt the exercise first** on the [`w1` branch](https://github.com/lassebenni/hyf-data-track-python-exercises/tree/w1) (starters only — no spoilers).
2. **When you're done, or genuinely stuck after 30 minutes**, switch to this branch:
   ```bash
   git fetch origin
   git checkout w1-solutions
   ```
   Or open the file directly on GitHub: each `solution.py` is browsable in the file tree above.
3. **Read `solution.py`, don't copy it.** Every design choice carries a `# WHY ...:` comment explaining the trade-off, the gotcha it sidesteps, or the production-readiness habit it teaches. The whole point of the reference solution is the *commentary*, not the code.

## Solution-file conventions

All six `solution.py` files follow the same shape:

- **Top docstring**: what the exercise teaches and why the trap matters.
- **`# WHY ...:` comments** at every non-obvious decision (encoding choices, exception types caught, loop structure, log-level selection, type-hint rationale).
- **Back-references to the Week 1 gotchas** when the trap is one of the documented ten (e.g., Gotcha #2 floats, Gotcha #8 print-vs-logging, Gotcha #10 cast-at-the-boundary).
- **Expected output** noted in a comment so you can sanity-check your own version against the reference.

## Local setup (if you prefer your own VS Code over Codespaces)

```bash
git clone -b w1-solutions https://github.com/lassebenni/hyf-data-track-python-exercises.git
cd hyf-data-track-python-exercises
code .
```

You'll need Python 3.11+. `exercise_5/` ships a `requirements.txt`; install with `pip install -r requirements.txt` from inside that subfolder first.
