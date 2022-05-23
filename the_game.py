# importing libraries and functions from another file
import random
from extras import show_hidden_word
from extras import choose_word
from extras import check_win
from extras import show_hidden_word
from extras import HANGMAN_PHOTOS
from extras import WIN_PHOTO


opening_title = 'Welcome to the game Hangman'
HANGMAN_ASCII_ART = (""" 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                      """)
MAX_TRIES = 6
old_letters_guessed = []

# making an opening to the game
print(opening_title,'\n',HANGMAN_ASCII_ART)
print("You need to guess the secret word, letter by letter.\nyou have 6 wrong attemps.\n")
print("GOOD LUCK!")

# choosing the secret words from another file
secret_word = choose_word("/Users/marygrankin/Documents/python/Hangman_game/words.txt")
print(show_hidden_word(secret_word, old_letters_guessed))

# covering possible wrong input options
num_of_tries = 0
while check_win(secret_word , old_letters_guessed) == False:
    guessed_letter = input("Guess a letter: ")
    print("\n")
    if len(guessed_letter) > 1:
        print("Sorry, I think you wrote more than one letter. Please try again")
    elif not guessed_letter.isalpha():
        print("Sorry, I think you didn't write a letter. Please try again")
    elif guessed_letter in old_letters_guessed:
        print("You have already tried this letter, please try another one")

    # adding the letter to the list of guessed letters 
    else:
        old_letters_guessed.append(guessed_letter.lower()) 
        if guessed_letter in secret_word:
            print("The letters you guessed: ", old_letters_guessed)
            print("\n")
            print(show_hidden_word(secret_word, old_letters_guessed))
            print("\n")
        else:
            num_of_tries += 1
            print(HANGMAN_PHOTOS[num_of_tries])

            # end of the game duo to a lose
            if num_of_tries == MAX_TRIES:
                print(" ")
                print("You lost, good luck next time :(")
                print(" ")
                print("BTW the word was: ", secret_word)
                print(" ")
                break

            # showing the added letters in the list and in the hidden word
            else:
                print("\n")
                print("The letters you guessed: ", old_letters_guessed)
                print("\n")
                print(show_hidden_word(secret_word, old_letters_guessed))
                print("\n")

                # printing without English mistakes
                if MAX_TRIES - num_of_tries == 1:
                    print("You have", MAX_TRIES - num_of_tries, "try left")
                else:
                    print("You have", MAX_TRIES - num_of_tries, "tries left")

# incase of a win
if check_win(secret_word , old_letters_guessed) == True:
    print("You Found the secret word and won the game!\nCongrats!")
    print(random.choice(WIN_PHOTO))