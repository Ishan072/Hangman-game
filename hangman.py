import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    count=len(secret_word)
    for i in letters_guessed:
        if (i in secret_word):
            count=count-secret_word.count(i)
    if(count==0):
        return True
    else:
        return False
    
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    letters_left="abcdefghijklmnopqrstuvwxyz"
    
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        a=letters_left.index(i)
        letters_left=letters_left[:a]+letters_left[a+1:]
    return letters_left

def hangman_images(count):
    return IMAGES[count]

def isvalid(s,available_letters):
    if(len(s)!=1 or not s.isalpha() or s not in available_letters):
        return False
    
    return True

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    lives=8
    count=-1
    letters_guessed = []
    while (lives!=0):
        print("\n\t Lives left :",lives)
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        if(isvalid(guess,available_letters)==False):
            print("\t\nINVALID INPUT")
            continue
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            if(lives!=8):
                print(hangman_images(count))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            lives-=1
            count+=1
            print("Oops! That letter is not in my word: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("\n\t",hangman_images(count))
            print("")
    if(lives==0):
        print("\n\t GAME OVER")
        print("\n\t YOU LOST")

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
