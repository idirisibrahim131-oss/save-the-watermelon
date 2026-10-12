"""Functions for checking guesses and updating the game."""

import random


def choose_word(words):
    """Pick a word from the list."""
    if not words:
        raise ValueError("The word list is empty.")
    return random.choice(words).lower()


def display_word(secret_word, guessed_letters):
    """Show guessed letters and underscores for the letters not guessed yet."""
    shown_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            shown_letters.append(letter)
        else:
            shown_letters.append("_")
    return " ".join(shown_letters)


def validate_guess(raw_guess, guessed_letters):
    """Check if the player entered one new letter from A to Z."""
    guess = raw_guess.strip().lower()

    if len(guess) != 1:
        return False, guess, "Please enter one letter at a time."
    if not guess.isalpha() or not guess.isascii():
        return False, guess, "Please enter a letter from A to Z."
    if guess in guessed_letters:
        return False, guess, "You already tried that letter. Pick another one."

    return True, guess, ""


def word_is_revealed(secret_word, guessed_letters):
    """Return True if the player has guessed every letter in the word."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def process_guess(secret_word, guess, guessed_letters, slices_left):
    """Save the guess and take a slice away if it is wrong."""
    guessed_letters.add(guess)

    if guess in secret_word:
        return slices_left, f"Good guess! {guess!r} is in the word."
    return slices_left - 1, f"Sorry, {guess!r} is not in the word."


def play_again():
    """Ask the player if they want another round."""
    while True:
        answer = input("\nDo you want to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")
