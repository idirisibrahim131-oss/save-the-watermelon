# Pseudocode

```text
Show the game title and rules

Ask the player to start a round
Pick a random word
Set guessed letters to an empty set
Set slices left to 6

While slices are left and the word is not solved:
    Show the hidden word and current status
    Ask the player for one letter
    Change the guess to lowercase and remove extra spaces

    If the guess is not exactly one letter:
        Tell the player to enter one letter
    Else if it is not an A-Z letter:
        Tell the player to enter a letter
    Else if the player already guessed it:
        Tell the player to choose another letter
    Else:
        Save the guess
        If the letter is in the word:
            Tell the player it was correct
        Else:
            Take away one slice
            Tell the player it was wrong

If the whole word was guessed:
    Show the win message
Otherwise:
    Show the loss message and reveal the word

Ask if the player wants to play again
If yes, start another round
If no, say goodbye
```
