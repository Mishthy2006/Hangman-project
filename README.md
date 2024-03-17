Project Title: Hangman-Game

Team Members:
1. Manager - Mishthy Sharma
2. Developer - Palak Sharma
3. Tester - Liza 

Project Details: Version1 has been released by the developer at 12:00am IST(14-03-24).

Additional features to be required: Hangman is a classic word guessing game typically played between two people, but here user will play with the computer. Computer will draws a series of dashes, each representing a letter in the word. The user tries to guess the word by suggesting letters one at a time, but it needs some augumentation.

Clear instructions: To make our game more user friendly we will add some features in it like:
a) Visual Represantion of HAngman: If the guessed letter is not in the word, a portion of a hangman is drawn (usually a gallows, stick figure, or some other representation of a hanging person). The game continues until the guessing player successfully guesses the word or makes too many incorrect guesses, resulting in the full hangman being drawn.
This will make the game look more interesting.

b) Adding a Timer: We can add a timer in our game that certain minutes will be given to the user to guess the word, If in that given time user can not be able to guess then the user will loose the game. This will make pressure on the user and is a fun way to practice vocabulary or spelling skills.

Version 1.1:
In this iteration of the game, upon execution, it currently displays a blank window. To address this issue, the constructor method should be renamed to _init_ with double underscores at the beginning and end. The original code provided in version 1 utilizes init with single underscores, resulting in the constructor not being invoked when an instance of the class is created, thereby causing the blank window. After rectifying this error, an additional feature will be implemented. Following the conclusion of a game, a message box will prompt the user with the inquiry, "Would you like to play again?" The user will be presented with the options "Yes" or "No.

Version 1.2:
In Version 1.2 of the game, while errors are absent, there is a need for several enhancements to augment user engagement. Primarily, the current iteration lacks sufficient user interactivity. To address this, incorporating additional features to enhance user interaction is imperative. One proposed enhancement involves integrating a diagrammatic representation following each attempt, thereby enriching the user experience. Additionally, the current implementation of the word selection function within the code restricts the available options, resulting in repetitive gameplay experiences for users engaging with the game multiple times. To mitigate this issue, an expansion of the words are required in def choice function to ensure users to get a different word for guessing with each playthrough, thereby enhancing overall gameplay variability and user satisfaction.

Version 3:
In the forthcoming version, The interface shall be modified such that upon making a guess and appending the corresponding digit to the output box, the preceding character shall be removed prior to appending the subsequent one. This adjustment aims to enhance the clarity and tidiness of the displayed information. Although, This version is good but we can make it more appealing by introducing a new color scheme or introducing visually appealing colors to the interface. This enhancement seeks to create a more immersive and enjoyable user experience. Lastly, an additional feature to consider is the inclusion of a scoring mechanism. Upon the conclusion of each game session, the final score shall be displayed within the message box, providing users with feedback on their performance. This addition aims to further enrich the user experience and encourage continued engagement with the application. These alterations can significantly enhance the interactivity, appeal, and overall quality of the game.

Version 4:
Version 4 has been thoroughly updated with a variety of improvements and additional features, rendering it exceedingly user-friendly and an enjoyable game to engage with. A novel color scheme has been integrated to enhance its visual appeal to users. Notably, the game now incorporates diagrammatic representations following each incorrect guess, aiding players in visualizing their progress. Furthermore, upon correctly guessing a word, the game provides a visual depiction of the word being formed. An added feature includes a "play again" button, allowing users to initiate a new game seamlessly at any point during play. To enrich user experience, an additional scoring system has been implemented, providing players with a countable measure of their performance at the conclusion of each game session. Importantly, the game fosters interactivity through message boxes that appear after every guess and upon completion of a game. This version has been extensively tested and is now deemed error-free, making it the final version of the game.
