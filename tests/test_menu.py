from pick_one.menu import parse_choice, run_menu


def test_parse_choice_accepts_valid_numbers():
    assert parse_choice("1") == "1"
    assert parse_choice(" 4 ") == "4"


def test_parse_choice_rejects_invalid_input():
    assert parse_choice("") is None
    assert parse_choice("5") is None
    assert parse_choice("abc") is None


def run_with_inputs(inputs):
    answers = iter(inputs)
    output = []
    run_menu(input_fn=lambda prompt: next(answers), print_fn=output.append)
    return output


def test_quit_ends_menu():
    output = run_with_inputs(["4"])
    assert output[-1] == "Bye!"


def test_invalid_choice_shows_message_and_menu_continues():
    output = run_with_inputs(["9", "4"])
    assert "Please enter a number from 1 to 4." in output
    assert output[-1] == "Bye!"


def test_game_choice_returns_to_menu():
    output = run_with_inputs(["2", "4"])
    assert "Spinner is coming soon." in output
    assert output.count("\n=== Pick-One ===") == 2
