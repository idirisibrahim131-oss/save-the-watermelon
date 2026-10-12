# Save the Watermelon

Save the Watermelon is a small word guessing game I made in Python. The computer picks a word, and the player tries to guess it one letter at a time. You start with six watermelon slices. Each wrong letter costs one slice, so try to figure out the word before you run out.

## How to run it

You need Python 3 installed. Open a terminal in this folder and type:

```bash
python3 src/game.py
```

On some computers, `python src/game.py` may work instead.

## Rules

- Guess one letter at a time.
- Uppercase and lowercase letters are treated the same.
- A correct letter shows up in the word and does not cost a slice.
- A wrong letter costs one slice.
- A blank guess, more than one character, or a letter you already guessed does not cost a slice.
- The game ends when you reveal the word or run out of slices.
- At the end, you can choose to play again.

## Files

- `src/game.py` runs the game and prints the information on the screen.
- `src/logic.py` has the functions that check guesses and update the game.
- `src/words.py` is the list of words the game can choose from.
- `docs/` has the design, pseudocode, and test plan for the project.

## One thing to know

The word is picked randomly, so it may be different each time you play. The test plan has spaces for actual results because those should be filled in after running the tests.
