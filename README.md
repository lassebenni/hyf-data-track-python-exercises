# HYF Data Track — Week 1 Practice Exercises

Six small exercises that consolidate Week 1 (variables, functions, type hints, logging, debugging, file I/O, CLI). Pick the ones that match what felt shaky on a first read of the chapter; you can do them in any order.

## Layout

Each exercise lives in its own subfolder so you can open a single Codespace and switch between them.

| Folder | Topic | Concepts |
|---|---|---|
| [`exercise_1/`](exercise_1/) | The Temperature Logger | Variables, functions, type hints, logging |
| [`exercise_2/`](exercise_2/) | The Data Cleaner | Lists, loops, conditionals, debugging |
| [`exercise_3/`](exercise_3/) | The Precision Trap | Floating-point math, debugger usage |
| [`exercise_4/`](exercise_4/) | Grade Processor | Dictionaries, type hints, logging, branching |
| [`exercise_5/`](exercise_5/) | The File Ingestor | File I/O, context managers, strings |
| [`exercise_6/`](exercise_6/) | The Pipeline CLI | argparse, logging levels, pathlib |

## Two ways to run

### A. Codespace (zero setup, runs in browser)

Each Week 1 chapter that references a specific exercise links directly into the right folder via:

```
https://github.com/codespaces/new/lassebenni/hyf-data-track-python-exercises?ref=w1&folder=exercise_N
```

Inside the Codespace, all six exercises are available. The shared `.devcontainer/` at the repo root sets up Python 3.11 + the VS Code Python extensions for every folder.

### B. Local clone (use your own VS Code)

Prefer your own editor and toolchain? Clone the `w1` branch once:

```bash
git clone -b w1 https://github.com/lassebenni/hyf-data-track-python-exercises.git
cd hyf-data-track-python-exercises
code .
```

Then open whichever exercise folder you want from the VS Code Explorer (`exercise_1/`, `exercise_2/`, ...). You'll need Python 3.11+ installed locally; `exercise_5/` and any future exercise that ships a `requirements.txt` will need `pip install -r requirements.txt` from inside that subfolder first.

## Reset a single exercise

If you've made a mess of one folder and want a clean slate, reset only that subfolder rather than wiping the whole workspace:

```bash
git checkout -- exercise_3/
```

That gives you the original starter files for Exercise 3 without touching your work in the other folders.

## Reference solutions

Reference solutions for **all six exercises** live on a separate branch, [`w1-solutions`](https://github.com/lassebenni/hyf-data-track-python-exercises/tree/w1-solutions). This branch (`w1`) is intentionally starter-only so you don't accidentally peek before you've struggled.

When you're done with an exercise (or genuinely stuck after ~30 minutes), switch:

```bash
git fetch origin
git checkout w1-solutions
```

Each `solution.py` carries `# WHY ...:` comments explaining every design choice — read the comments, don't just copy the code.
