# HYF Data Track — Week 1 Practice Exercises *(with reference solutions)*

> ⚠️ **You're on the `w1-solutions` branch.** Each exercise's starter file (`exercise.py` / `exercise_2.py` / `exercise_6.py` / `assignment_6.py`) has been **filled in with the answer in-place**. The original TODO / FIXME comments from the starter are still there, with the solution code and a `# WHY ...:` note sitting directly under each one. Open this branch AFTER you've attempted the exercises on `w1` — the whole point of the practice block is the struggle, not the answer key.
>
> If you landed here by mistake and want clean starters: switch to the [`w1` branch](https://github.com/lassebenni/hyf-data-track-python-exercises/tree/w1).

Six small exercises that consolidate Week 1 (variables, functions, type hints, logging, debugging, file I/O, CLI). Pick the ones that match what felt shaky on a first read of the chapter; you can do them in any order.

## Layout

Each exercise lives in its own subfolder. The single starter file in each folder has been turned into the reference solution: original TODOs preserved, answer code + WHY comments added underneath.

| Folder | Topic | Concepts | File |
|---|---|---|---|
| [`exercise_1/`](exercise_1/) | The Temperature Logger | Variables, functions, type hints, logging | `exercise.py` |
| [`exercise_2/`](exercise_2/) | The Data Cleaner | Lists, loops, conditionals, debugging | `exercise_2.py` |
| [`exercise_3/`](exercise_3/) | The Precision Trap | Floating-point math, debugger usage | `exercise.py` |
| [`exercise_4/`](exercise_4/) | Grade Processor | Dictionaries, type hints, logging, branching | `exercise.py` |
| [`exercise_5/`](exercise_5/) | The File Ingestor | File I/O, context managers, strings | `assignment_6.py` |
| [`exercise_6/`](exercise_6/) | The Pipeline CLI | argparse, logging levels, pathlib | `exercise_6.py` (+ `data/`) |

## How to use this branch

1. **Attempt the exercise first** on the [`w1` branch](https://github.com/lassebenni/hyf-data-track-python-exercises/tree/w1) (starters only — no spoilers).
2. **When you finish, or genuinely stuck after ~30 minutes**, open the matching file on this branch (in your browser, or via `git checkout w1-solutions` locally — see *Spoiler discipline* below).
3. **Read the WHY comments, do not copy the code verbatim.** Every design choice carries a `# WHY ...:` note explaining the trade-off, the gotcha it sidesteps, or the production-readiness habit it teaches. The whole point of the reference solution is the *commentary*, not the code.

## Solution-file conventions

All six solution files follow the same shape:

- **Top docstring**: notes that the file is the in-place reference solution and what the exercise teaches.
- **Original `# TODO` / `# FIXME` comments preserved verbatim** so you can see the question and the answer side-by-side.
- **`# WHY ...:` comments** at every non-obvious decision (encoding choices, exception types caught, loop structure, log-level selection, type-hint rationale).
- **Back-references to the Week 1 gotchas** when the trap is one of the documented ten (e.g., Gotcha #2 floats, Gotcha #8 print-vs-logging, Gotcha #9 input-vs-argparse, Gotcha #10 cast-at-the-boundary).
- **Expected output** noted in a comment so you can sanity-check your own version against the reference.

## Spoiler discipline

If you have uncommitted edits in the matching subfolder on the `w1` branch, `git checkout w1-solutions` will refuse with `"Your local changes ... would be overwritten by checkout"`. That is Git protecting your work, not breaking it. Commit your attempt (or `git stash`) first, then switch.

To browse a single solution **without switching branches at all**, open it directly on GitHub from the file tree above.

## Local setup (if you prefer your own VS Code over Codespaces)

```bash
git clone -b w1-solutions https://github.com/lassebenni/hyf-data-track-python-exercises.git
cd hyf-data-track-python-exercises
code .
```

You'll need Python 3.11+. `exercise_5/` ships a `requirements.txt`; install with `pip install -r requirements.txt` from inside that subfolder first.
