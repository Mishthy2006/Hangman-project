Project Title: Hangman-Game

Team Members:
1. Manager - Mishthy Sharma
2. Developer - Palak Sharma
3. Tester - Liza Julaha

Project Details: Version1 has been released by the developer at 12:00am IST(14-03-24).

Additional features to be required: Hangman is a classic word guessing game typically played between two people, but here user will play with the computer. Computer will draws a series of dashes, each representing a letter in the word. The user tries to guess the word by suggesting letters one at a time, but it needs some augumentation.

Clear instructions: To make our game more user friendly we will add some features in it like:
a) Visual Represantion of HAngman: If the guessed letter is not in the word, a portion of a hangman is drawn (usually a gallows, stick figure, or some other representation of a hanging person). The game continues until the guessing player successfully guesses the word or makes too many incorrect guesses, resulting in the full hangman being drawn.
This will make the game look more interesting.

b) Adding a Timer: We can add a timer in our game that certain minutes will be given to the user to guess the word, If in that given time user can not be able to guess then the user will loose the game. This will make pressure on the user and is a fun way to practice vocabulary or spelling skills.

Version 1.1:
In this iteration of the game, upon execution, it currently displays a blank window. To address this issue, the constructor method should be renamed to _init_ with double underscores at the beginning and end. The original code provided in version 1 utilizes init with single underscores, resulting in the constructor not being invoked when an instance of the class is created, thereby causing the blank window. After rectifying this error, an additional feature will be implemented. Following the conclusion of a game, a message box will prompt the user with the inquiry, "Would you like to play again?" The user will be presented with the options "Yes" or "No.
