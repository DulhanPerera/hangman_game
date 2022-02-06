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

#### 2.2Get random words
Get word function is used to get a random word from the list named random. And this function returns the selected random word in uppercase. 

#### 2.3 Main Program Function

 
This function is the main part used in this game. In this function, number of turns you have to guess the letter is equal to number of letters in that word. And in the while loop word letters printing with the underscore and asking user input for the letters if you couldn’t guess the correct letter then one live (turn) decrease. The using global variables program counts the lost and win count.


Explanation :
In this code first I imported all the modules and packages. Such as import sys for run this code in console, import random for get random word from the word list, import string for uppercase characters and other things, and I also create another module and insert 4 python files to that module folder that codes are create table in SQL code, create database in SQL code, and insert and view data from the database codes. The I created variables in man python code.
# Create Database and the table for the game
createData = str(input("Do you want to create database for this ('y' for yes, 'n' for no): "))
if createData == 'y' or createData == 'Y':
    sub.createDatabase.create_database()
    sub.createTable.newTable()
    print("Database Created.")
else:
    pass

And this is the code that used to create database and able in the phpMyAdmin and this code only calling function in the module. And if user don’t want to create a database and table, this if else statement helps to if user wants create those do that or if user don’t want to do it this statement helps to pass to the next line in the code.
# Function for get random word
def get_word(words):
    word = random.choice(words)  # randomly chooses word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
this piece of code used for getting a random word from the list that I created as a module file and this function used for getting a random word and return the whole word in to uppercase.
# Function for run the main programme
def hangman():
    word = get_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used = set()  # what the user has guessed

    lives = len(word)

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) -> 'a b cd'
        print(lives, 'turns remain \nLetters Used:', ' '.join(used)) 

        # what current word is (ie. W - R D)
        word_list = [letter if letter in used else '_' for letter in word]
        print('Word: ', ' '.join(word_list))

        user_letter = input('Letter: ').upper()
        if user_letter in alphabet - used:
            used.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                # takes away a life if wrong
        elif user_letter in used:
            print('You have already used that letter. Guess another letter.')
        else:
            print('That is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    
    global lost
    global win
    if lives == 0:
        print('You lost! The word is ', word)
        lost=lost+1
    
    else:
        print('You won! The word is ', word)
        win=win+1

hangman()

this is the main function in this code, and this used for the main things in the hangman game. And in this function the turns you have to enter correct word is equal to length of the randomly selected word.
This function used for getting user inputs such as letter user guessed. And the lost and win is always count by this function and it also track how many times you played this game.
  Repaly the game using while 
re_play = str(input("Do you want to paly again (if yes type 'Y' or if No type 'N'): "))
    
count = 1 # Count how many times played this game

while(re_play == 'y'):
    hangman()
    count = count + 1
    
    re_play = str(input("Do you want to paly again (if yes type 'Y' or if No type 'N'): "))
    
print("\nYou played this game only", count, "times.\n")
print("You won this game only", win ,"times.\n")
print("You lost this game only", lost ,"times.\n")

this part used for if user wants to play the game again user can type ‘y’ and play this game again. Print the total played times and wins and losses. 

all_data = [user_name, win, lost, count]
  print(all_data)
  Inserting data to the database
sub.insert.insertFunc(all_data)

  Showing past record data in the database
showData = str(input("\nDo you want to view past game records (Yes == 'y' or 'Y' and No == 'n' or 'N')? "))
if showData == 'Y' or showData == 'y':
    print("\n")
    sub.viewData.view_details()
    print("\nGame Finished.")
else:
    print("Game Finished.")
This code part is used for inserting all data from the game to the database. And there’s an if else statement for show data if user wants or not.



