# hangman_game
## Single Payer game.
### Summery

Hangman is a paper and pencil guessing game played by two or more people. One player thinks a word, phrase, or sentence, and the other players must try to guess. They do this by saying the letters or numbers that they think are in the name. The name is displayed as a dash line. When a guessing player gives a letter or number in a word, the other player writes the letter or number in the places where they are in the name. If the letter or number is not in the name, the other player draws part of the image of the hanging man as a mathematical symbol (the type of number used for counting).
The game ends when:
•	The guessing player completes the word, or correctly guesses the whole word.
•	The other player completes the diagram of the hanged man.

In this python program the guessing player is the user and the player who complete the diagram is the python program.

### 1.	Introduction

#### 1.1 What is hangman game?

The word guess is represented by a dash line, representing each letter of the word. In many varieties, real names, such as names, places, and products, are not allowed. Slang words, sometimes called informal or abbreviated words, are also not allowed. When a guessing player lifts a letter from a word, the other player writes it in all its appropriate places. If the raised letter does not occur in the name, another player draws one part of the hanging stick as a mathematical symbol. A word guesser can, at any time, try to guess the whole word. If the name is correct, the game is over, and the guesser wins. If not, another player may choose to punish the guesser by adding something to the drawing. On the other hand, if a guesser makes a bad enough guess to allow another player to complete a drawing, the guesser loses. However, the guesser can also win by guessing all the letters from the word, thus completing the word, before the drawing is completed.

#### 1.2 About the hangman python program

This python program is a console program that allow user to guess the missing letters in the word that randomly give by the python program. And this program gives you the many options when you start to play this game like options to play this game again and again many times as you want. And after user finished playing this game this program will use your game data and uploaded it to the database that created for this game. If user want to view his past records, user can view those after the game ended. 

### 2.	Hangman Python Game

#### 2.1 Import Modules and Libraries


In this screenshot I used modules to run program easily.
1.	Import random – This used for importing randomly selected word from the word list to the program.
2.	Import sub.insert – Sub is the module that used to insert game data to the database.
3.	Import words – This is a module that contains 20 words in a list named words.
4.	Import string – This used for uppercasing every letter user get while the code running and capitalized every letter user inputs. 
5.	Import viewData – This is the module that used to view data in the database and this data display only if the user wants to view.

####2.2Get random words
Get word function is used to get a random word from the list named random. And this function returns the selected random word in uppercase. 

####2.3 Main Program Function

 
This function is the main part used in this game. In this function, number of turns you have to guess the letter is equal to number of letters in that word. And in the while loop word letters printing with the underscore and asking user input for the letters if you couldn’t guess the correct letter then one live (turn) decrease. The using global variables program counts the lost and win count.





