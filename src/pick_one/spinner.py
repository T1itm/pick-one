"""Spinner game: pick one item at random."""

import random

MIN_ITEMS = 2
MAX_ITEMS = 12


def parse_items(text):
    """Split text by commas or new lines, trim spaces, and drop empty items."""
    parts = text.replace("\n", ",").split(",")
    return [part.strip() for part in parts if part.strip()]


def validate_items(items):
    """Return an error message if the number of items is not allowed, otherwise None."""
    if len(items) < MIN_ITEMS:
        return f"Please enter at least {MIN_ITEMS} items."
    if len(items) > MAX_ITEMS:
        return f"Please enter at most {MAX_ITEMS} items."
    return None


def spin(items, rng=random):
    """Pick one item at random."""
    return rng.choice(items)


def play(input_fn=input, print_fn=print, rng=random):
    """Ask for items, then spin once and show the result."""
    print_fn("\n=== Spinner ===")
    print_fn(f"Enter {MIN_ITEMS}-{MAX_ITEMS} items separated by commas.")
    while True:
        items = parse_items(input_fn("Items: "))
        error = validate_items(items)
        if error is None:
            break
        print_fn(error)
    result = spin(items, rng)
    print_fn(f"The spinner picked: {result}")
    return result
