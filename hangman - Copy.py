import random   # For get random word 
import sub.insert   # Insert play data to database
from words import words   # Get words from the word list
import string   # For get correct outputs and get word in uppercase
import viewData   # View the database table

# Create Variables
user_name = ''
re_paly = ''
count = 0
lost = 0
win = 0
all_data = []
showData = ''

# User Details and instructions

print("\t\t========= HANGMAN ===========")

print("\t\t\tGame Rules!\n > Number of turns equal to letters in a word.\n > You can play many times.\n")

user_name = str(input("Enter player name: "))

# Function for get random word
def get_word(words):
    word = random.choice(words)  # randomly chooses word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


# Function for run the main programme
def hangman():
    word = get_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = len(word)

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(lives, 'lives remain \nLetters Used:', ' '.join(used_letters)) # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Word: ', ' '.join(word_list))

        user_letter = input('Letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
        elif user_letter in used_letters:
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



# Repaly the game using while 
re_play = str(input("Do you want to paly again (if yes type 'Y' or if No type 'N'): "))
    
count = 1 # Count how many times played this game

while(re_play == 'y'):
    hangman()
    count = count + 1
    
    re_play = str(input("Do you want to paly again (if yes type 'Y' or if No type 'N'): "))
    
print("\nYou played this game only", count, "times.\n")
print("You won this game only", win ,"times.\n")
print("You lost this game only", lost ,"times.\n")

all_data = [user_name, win, lost, count]
print(all_data)

sub.insert.insertFunc(all_data)

# Showing past record data
showData = str(input("\nDo you want to view past game records (Yes == 'y' or 'Y' and No == 'n' or 'N')? "))
if showData == 'Y' or showData == 'y':
    viewData.view_details()
else:
    print("Game Finished.")






    
