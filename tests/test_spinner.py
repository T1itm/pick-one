import random

from pick_one.spinner import parse_items, play, spin, validate_items


def test_parse_items_splits_and_trims():
    assert parse_items(" Dongjun, Seungho ,Minsu ") == ["Dongjun", "Seungho", "Minsu"]


def test_parse_items_accepts_new_lines_and_ignores_empty_items():
    assert parse_items("A\nB,, \nC") == ["A", "B", "C"]


def test_validate_items_rejects_too_few_or_too_many():
    assert validate_items(["A"]) == "Please enter at least 2 items."
    assert validate_items([str(n) for n in range(13)]) == "Please enter at most 12 items."
    assert validate_items(["A", "B"]) is None


def test_spin_always_returns_an_item_from_the_list():
    items = ["A", "B", "C"]
    rng = random.Random(1)
    for _ in range(100):
        assert spin(items, rng) in items


def test_spin_is_repeatable_with_same_seed():
    items = ["A", "B", "C", "D"]
    assert spin(items, random.Random(42)) == spin(items, random.Random(42))


def test_every_item_can_be_picked():
    items = ["A", "B", "C"]
    rng = random.Random(7)
    picked = {spin(items, rng) for _ in range(300)}
    assert picked == set(items)


def test_play_asks_again_after_invalid_input():
    answers = iter(["only one", "A, B"])
    output = []
    result = play(
        input_fn=lambda prompt: next(answers),
        print_fn=output.append,
        rng=random.Random(0),
    )
    assert "Please enter at least 2 items." in output
    assert result in ["A", "B"]
    assert output[-1] == f"The spinner picked: {result}"
