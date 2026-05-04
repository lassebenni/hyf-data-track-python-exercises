"""Reference solution for Week 1 Exercise 1: The Temperature Logger.

Teaches: production-ready function shape — type hints + structured
logging instead of print().

Why it matters: print() is for one-shot scripts and notebooks. Logging
is for code anyone else will run, monitor, or debug at 3am after the
operator has gone home (Gotcha #8: Print vs Logging). The whole
exercise is one tiny function, but it carries every habit a junior
data engineer has to internalise on day one.
"""
import logging

# WHY level=INFO: matches the assignment level. INFO + WARNING + ERROR
# are visible by default; DEBUG is hidden unless explicitly enabled.
# INFO is the right baseline for a normal-looking pipeline — loud
# enough to confirm it ran, quiet enough not to bury real warnings.
logging.basicConfig(level=logging.INFO)


def convert_c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using the standard formula.

    WHY type hints (Ch5): the signature documents what the caller
    must pass and what they get back, so an IDE / mypy can flag
    `convert_c_to_f("hot")` as wrong before the script runs. The
    Python runtime does NOT enforce them; they are pure documentation
    that tooling reads. They cost nothing to add and pay back every
    time someone else (or future-you) reads the function.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    # WHY logging.info BEFORE returning: capture the conversion every
    # time the function is called so an operator can audit the
    # pipeline's behaviour after the fact. Returning silently would
    # discard that signal — exactly the "silent failure" trap from
    # Gotcha #8.
    logging.info(f"Converting {celsius}°C to {fahrenheit}°F")
    return fahrenheit


# WHY three calls covering 0 / 25 / 100: freezing point, room
# temperature, boiling point. Quick visual check that each conversion
# produces a sensible number (32, 77, 212).
convert_c_to_f(0)
convert_c_to_f(25)
convert_c_to_f(100)
