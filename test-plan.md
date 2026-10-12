# Test Plan

I will use these tests to check that the game works. The expected result is what I think should happen. After I run each test, I need to write what actually happened and mark whether it passed.

To make a test easier to repeat, I can temporarily use a known word while testing. I should put the normal random word selection back before I submit the project.

| Test | What I try | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Correct letter | Guess a letter that is in the word | The letter appears and no slice is lost | Fill in after testing | Pending |
| Wrong letter | Guess a letter not in the word | One slice is removed | Fill in after testing | Pending |
| Capital letter | Enter `A` when `a` is in the word | It is treated like `a` | Fill in after testing | Pending |
| Repeat guess | Guess `a`, then enter `A` again | The second guess is rejected and no slice is lost | Fill in after testing | Pending |
| Multiple letters | Enter `ab` | The game asks for one letter | Fill in after testing | Pending |
| Number | Enter `7` | The guess is rejected and no slice is lost | Fill in after testing | Pending |
| Punctuation | Enter `!` | The guess is rejected and no slice is lost | Fill in after testing | Pending |
| Blank guess | Press Enter without typing | The game asks for a letter | Fill in after testing | Pending |
| Win | Guess all letters in the secret word | A win message appears | Fill in after testing | Pending |
| Lose | Make enough wrong guesses to use all six slices | A loss message and the secret word appear | Fill in after testing | Pending |
| Play again | Answer `y` after a round | A new round starts | Fill in after testing | Pending |
| Quit | Answer `n` after a round | The game says goodbye and ends | Fill in after testing | Pending |
| Invalid replay answer | Enter `maybe` at the replay prompt | The game asks for y or n again | Fill in after testing | Pending |

## Problems I find

If a test does not work as expected, write down what happened, fix the problem, and run the test again. Do not mark a test as passed until it has been tried.
