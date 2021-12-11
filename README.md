# card_games
Command line card games written in Python

## Files

#### main.py

- Run file to start
- Displays a menu, handles input, then starts the game that was selected by the user
- The game object then handles game play and input from there

#### cards.py

- Contains some utility classes (Deck, Card, Player) that are likely to be used by any game

#### menu.py

- Contains the functionality for displaying a menu on the command line
- Also takes care of handling input and returning the user's selection in the form of an index into an array of items. Menu starts at 1 but return value (index) starts at 0.

#### war.py / (game).py

- Object representing a game
- Should contain all of the logic for running the game and handling user input
- Currently only 'war.py' exists, but other games that are added should probably be something like game_name.py

## To add a game

- Create a game object e.g. `class Poker:` in a file called `poker.py`
- Object must have a `__str__` function in order to display in on the menu
- Object must have a `GameLoop(self)` function which will be called from `main.py` and will give control to the game object to handle the game play
- Other than the above 2 must have requirements, the game object can do whatever it needs to, use any helper functions/classes necessary to play the game
