"""Main part of Save the Watermelon."""

from words import WORDS
from logic import (
    choose_word,
    display_word,
    validate_guess,
    word_is_revealed,
    process_guess,
    play_again,
)

STARTING_SLICES = 6


def show_header():
    """Print the title and explain the rules."""
    print("\n" + "=" * 40)
    print("       SAVE THE WATERMELON")
    print("=" * 40)
    print("Guess the hidden word one letter at a time.")
    print(f"You start with {STARTING_SLICES} slices.")
    print("A wrong guess costs one slice.\n")


def show_status(secret_word, guessed_letters, slices_left):
    """Print the current word, guessed letters, and slices left."""
    print("\nWord: " + display_word(secret_word, guessed_letters))
    print("Slices left: " + "🍉 " * slices_left + "· " * (STARTING_SLICES - slices_left))
    if guessed_letters:
        print("Letters tried: " + ", ".join(sorted(guessed_letters)))
    else:
        print("Letters tried: none")


def play_round():
    """Play one round until the player wins or runs out of slices."""
    secret_word = choose_word(WORDS)
    guessed_letters = set()
    slices_left = STARTING_SLICES

    while slices_left > 0 and not word_is_revealed(secret_word, guessed_letters):
        show_status(secret_word, guessed_letters, slices_left)
        raw_guess = input("\nGuess a letter: ")
        valid, guess, message = validate_guess(raw_guess, guessed_letters)

        if not valid:
            print(message)
            continue

        slices_left, message = process_guess(
            secret_word, guess, guessed_letters, slices_left
        )
        print(message)

    show_status(secret_word, guessed_letters, slices_left)
    if word_is_revealed(secret_word, guessed_letters):
        print("\nYou saved the watermelon! You guessed the word.")
    else:
        print("\nThe watermelon ran out of slices. You lost this round.")
        print(f"The word was: {secret_word}")


def main():
    """Start the game and ask if the player wants to keep playing."""
    show_header()
    while True:
        play_round()
        if not play_again():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
