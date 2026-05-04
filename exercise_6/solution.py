"""Reference solution for Week 1 Exercise 6: The Pipeline CLI.

Teacher-facing reference. NOT shipped to the student exercise repo
(students should land on the starter at the `w1-ex6` branch and
solve it themselves; this file exists so the teacher can paste a
working answer during the walk-through).

The exercise asks students to:
  1. Wrap the script with argparse so it accepts --input, --output,
     and --log-level.
  2. Configure the root logger to the chosen level.
  3. Pick the right log level for each kind of message in clean_rows().
  4. Wire args.input / args.output into the file I/O.

Run:
    python week_1__ex6_solution.py \
        --input data/messy_users.csv \
        --output cleaned.json \
        --log-level DEBUG
"""
import argparse
import csv
import json
import logging


def clean_rows(rows):
    """Clean each row: trim name, lowercase email, drop nameless rows."""
    cleaned = []
    skipped = 0

    for i, row in enumerate(rows):
        # WHY DEBUG: per-row trace is only useful when hunting a bug.
        # On a real pipeline with 100k rows this would drown the log
        # and slow the run. Rule of thumb: "would I want to see this
        # on a clean run?" No -> DEBUG.
        logging.debug(f"row {i}: starting")

        if not row.get("name", "").strip():
            # WHY WARNING: skipped rows are a data-quality signal the
            # operator should know about, but they do not crash the
            # pipeline. WARNING is the level that says "look at me,
            # but I am not breaking."
            logging.warning(f"row {i}: missing name, skipping")
            skipped += 1
            continue

        # Cast / clean at the boundary (Gotcha #10): once the values
        # have the right shape, the rest of the code can trust them.
        row["name"] = row["name"].strip()
        row["email"] = row.get("email", "").strip().lower()
        cleaned.append(row)

    # WHY INFO: a one-line summary is exactly what an operator wants
    # to see on every clean run ("yes, the pipeline did its job, here
    # are the numbers"). That is the textbook definition of INFO.
    logging.info(f"cleaned {len(cleaned)} rows, skipped {skipped}")
    return cleaned


def main():
    # WHY argparse: data-engineering scripts run under schedulers
    # (cron, Airflow, GitHub Actions), not humans. input() would block
    # forever waiting for a keystroke that never comes (Gotcha #9).
    parser = argparse.ArgumentParser(
        description="Clean a messy users CSV into a tidy JSON file."
    )
    # WHY required=True: there is no sensible default for an input
    # path. Failing fast with "missing --input" beats silently
    # processing the wrong file.
    parser.add_argument("--input", required=True, help="path to the messy CSV")
    parser.add_argument("--output", required=True, help="path to write JSON")
    # WHY choices=[...]: argparse rejects typos like "DEUBG" at parse
    # time with a friendly message, instead of crashing later inside
    # the logging module with a less obvious traceback.
    # WHY default="INFO": pipelines should be loud enough to confirm
    # they ran, quiet enough not to bury real warnings.
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    args = parser.parse_args()

    # WHY getattr(logging, "INFO"): log levels in the logging module
    # are module-level integer constants (logging.DEBUG = 10,
    # logging.INFO = 20, ...). argparse hands us the level as a
    # string; getattr looks up the matching constant. The choices=[...]
    # above guarantees the lookup always succeeds.
    logging.basicConfig(level=getattr(logging, args.log_level))

    # WHY `with open(...)`: the context manager closes the file even
    # if an exception fires inside the loop. Without `with`, a crash
    # mid-read leaves the file handle dangling (Ch9).
    with open(args.input) as f:
        # WHY list(...): csv.DictReader is a lazy iterator tied to the
        # open file. Materialising the rows up front lets us close
        # the file before the cleaning step starts.
        rows = list(csv.DictReader(f))

    cleaned = clean_rows(rows)

    with open(args.output, "w") as f:
        # WHY indent=2: JSON without indent is one giant line, painful
        # to diff or eyeball. indent=2 stays small but readable.
        json.dump(cleaned, f, indent=2)


if __name__ == "__main__":
    # WHY the guard: if anyone imports this module (for unit tests,
    # say), main() should not auto-run (Gotcha #6: import side-
    # effects). The guard makes the file behave as a script when run
    # directly and as a library when imported.
    main()
