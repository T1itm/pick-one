"""Main menu for Pick-One."""

GAMES = {"1": "Ladder", "2": "Spinner", "3": "Dice duel"}
QUIT = "4"


def parse_choice(text):
    """Return the menu choice if it is valid, otherwise None."""
    choice = text.strip()
    if choice in GAMES or choice == QUIT:
        return choice
    return None


def run_menu(input_fn=input, print_fn=print):
    """Show the menu until the user chooses Quit."""
    while True:
        print_fn("\n=== Pick-One ===")
        for key, name in GAMES.items():
            print_fn(f"{key}. {name}")
        print_fn(f"{QUIT}. Quit")

        choice = parse_choice(input_fn("Choose a game: "))
        if choice is None:
            print_fn("Please enter a number from 1 to 4.")
        elif choice == QUIT:
            print_fn("Bye!")
            return
        else:
            print_fn(f"{GAMES[choice]} is coming soon.")
