"""Reference solution for Week 1 Exercise 2: The Data Cleaner.

Teaches: cast at the boundary (Gotcha #10) + skip-rather-than-crash
defensive loops + the discipline of catching only the exceptions you
actually expect (not bare `except:`).

The starter crashes with `TypeError: unsupported operand type(s) for
+=: 'int' and 'str'` because the list mixes ints, numeric strings,
and a truly unparseable string. The fix:
  - convert numeric strings (`"40"`) to ints
  - skip strings that aren't numeric (`"not_available"`)
  - skip negative ages (impossible, so a data-quality error)
"""

ages = [25, 30, "40", "not_available", 20, -5]


def calculate_average_age(age_list):
    total = 0
    count = 0
    for age in age_list:
        # WHY try/except instead of isinstance + .isdigit(): the
        # values are heterogeneous (int OR str). A try/except handles
        # both kinds symmetrically — convert what we can, skip what
        # we can't. `.isdigit()` would also miss `"3.14"` or `"-5"`.
        try:
            value = int(age)
        except (ValueError, TypeError):
            # `int("not_available")` raises ValueError; `int(None)`
            # would raise TypeError. Catch both so a future dirtier
            # dataset doesn't silently start crashing. NEVER use
            # bare `except:` — it would swallow KeyboardInterrupt
            # and SystemExit too.
            continue

        # WHY the negative-skip AFTER the cast: doing all validation
        # in one place after the cast keeps the validation logic
        # together. A negative *string* like "-5" also gets caught
        # here (the cast succeeds, the value is < 0).
        if value < 0:
            continue

        total += value
        count += 1

    # WHY guard against count == 0: dividing by zero would crash with
    # ZeroDivisionError instead of returning a useful "no valid rows"
    # signal. Returning None makes the empty case loud at the call
    # site rather than silently returning 0 (which would be a
    # plausible-but-wrong answer).
    if count == 0:
        return None
    return total / count


# Expected: 28.75  (= (25 + 30 + 40 + 20) / 4 — "40" cast to int,
# "not_available" and -5 skipped)
print(calculate_average_age(ages))
