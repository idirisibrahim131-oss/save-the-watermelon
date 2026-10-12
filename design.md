# Design Notes

## What the game does

The game picks a word from a list and hides the letters with underscores. The player types a letter to try to uncover the word. There are six slices to start with, and every wrong guess takes one away.

## Rules I used

1. The game chooses a random word.
2. The player enters one letter at a time.
3. The game ignores uppercase versus lowercase.
4. A correct guess reveals that letter wherever it appears.
5. A wrong guess removes one slice.
6. Blank input, numbers, multiple characters, and repeated guesses are rejected without losing a slice.
7. The player wins by revealing the whole word and loses if all slices are gone.
8. After a round, the player can choose whether to play again.

## Main variables

- `secret_word` is the word the player is trying to guess.
- `guessed_letters` keeps track of the letters the player has tried.
- `slices_left` stores how many slices are left.
- `WORDS` is the list of words that can be selected.

## How I split up the code

I used three Python files so everything would not be in one big file. `game.py` handles the round and what gets printed. `logic.py` has functions for choosing the word, checking guesses, and deciding if the word is complete. `words.py` just holds the word list.

The game keeps asking for a guess while the player still has slices and has not guessed the whole word. It checks the input first so invalid guesses do not affect the score.
