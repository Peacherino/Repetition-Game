# Repetition Game
This is a pattern memorization game written in python with a GUI made using pyFLTK.

## Screenshot of Gameplay

## About Project:
I made this project for practice with making timed events that create game states.

In this project, the program and player take turns interacting with the same buttons. In order to
prevent players from interfering with the program's sequence, I had to make it so the player could not
interact with the buttons during the program's turn.

I used what I had learned in my earlier music-playlist project about subprocesses for the buttons' sound
effects. (should i put this in how it works?)

## How it works:
The game begins with 4 coloured buttons: red, blue, yellow, green.
One random button immediately plays signaling the start of the game. The player must click on the button
that played to begin the pattern.

The program adds a new random button after every successfully completed sequence, and plays the entire
sequence again. The player must repeat the increasingly long sequence each turn.

The game continues until the player recites the pattern incorrectly. A loud buzzer plays and the game
reveals how many turns the player took before losing. The game will give the player a button with the
option to restart and play a newly generated game.

#### The program has two modes that manage the different parts of the gameplay in the App class:
- Display mode: Program displays sequence of buttons, player can not interfere with buttons
- User Input mode: Allows player to interact with buttons to repeat sequence

FLTK timers are used to schedule the button flashing periods and switch between program and player mode.

## Challenges:
One of the biggest challenges I encountered when building this was organizing and separating the
responsibilities of the program into two classes.

I separated the actual button interactions and the game sequence and game mode tracker. This made
it a lot easier to organize and use all the button logic written in the GameButton class to be called
upon for everything in the App class.

Doing this was very useful for gaining experience in figuring out how to decide on seperating
classes by what components and preventing bugs in larger-scale games.

## Future improvements:
- Including a button to start the game so the game does not begin immediately on launch
- Implementing a cleaner exit to the game
- Offering difficulty levels with increased speed and changing button positions
- Making the GUI layout more aesthetically pleasing

## How to run it:
#### 1. Start the game
python3 pattern_game.py

#### 2. Gameplay
- watch and listen for the program to display a sequence
- click the buttons in the same order as the program once the sequence ends
- for every successful round, the sequence will introduce one more button to the pattern
- continue to repeat the sequence for as many turns as possible
- once an incorrect button is selected a buzzer will sound and the game will end
- your score will be displayed and the game will offer the option to restart

Resources Used:
- Python
- PyFLTK
- Python subprocess module
- Object-oriented programming
- Event-driven programming
