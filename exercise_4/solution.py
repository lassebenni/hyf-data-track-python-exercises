"""Reference solution for Week 1 Exercise 4: Grade Processor.

Teaches: dict access patterns + if/elif/else discipline + log-level
selection (INFO for normal flow, WARNING for action-needed signals).

The trap the chapter explicitly warns about: writing three separate
`if` blocks instead of an `if/elif/else` ladder. With three separate
ifs, an average of 85 satisfies "> 80" AND "> 60", so you log
"Grade A" AND "Grade B" for the same student — corrupting the
grading log. The `elif` is what makes the ladder pick exactly one
branch. Order matters: check the highest tier first.
"""
import logging

# WHY format=...: include a timestamp so an operator browsing the
# logs after the fact can correlate events across pipelines. The
# default format omits the timestamp — fine for an interactive REPL,
# bad for production. Timestamps are cheap and always worth adding.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def process_student(student_data: dict) -> None:
    """Log a grade tier for the student, exactly once."""
    name = student_data["name"]
    grades = student_data["grades"]

    logging.info(f"Processing grades for {name}")

    # WHY sum(grades) / len(grades): clearer than building a running
    # total in a loop for a small list. Use a loop only when you need
    # per-iteration side effects (logging each grade, validating each
    # entry, etc.) — otherwise prefer the built-ins.
    average = sum(grades) / len(grades)

    # WHY if/elif/else: exactly one branch fires. Three separate `if`
    # statements would fire two when average > 80 (both "> 80" and
    # "> 60" are true), corrupting the grading log. The order matters
    # — check the highest tier first so the ladder narrows correctly.
    if average > 80:
        logging.info("Grade A")
    elif average > 60:
        logging.info("Grade B")
    else:
        # WHY WARNING (not INFO): this is the level that says "look
        # at me, an operator should know about this" without being a
        # crash. A struggling student is data-quality / pedagogical
        # signal: the teacher should see it but the script keeps
        # running. INFO would let it blend into normal traffic; ERROR
        # would imply something broke.
        logging.warning("Student requires assistance")


student = {"name": "Alice", "grades": [85, 90, 78]}
process_student(student)
# Expected (one line, single tier): "Processing grades for Alice" +
# "Grade A" (Alice's average is ~84.3, which is > 80).
