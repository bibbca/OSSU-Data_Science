# Problem Set 2, hangman.py
# Name: Caleb Bibb
# Collaborators:
# Time spent: 5 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    is_solved = True
    for letter in secret_word:
        if letter not in letters_guessed:
            is_solved = False
    return is_solved



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    partial_string = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            partial_string = partial_string + "_ "
        else:
            partial_string = partial_string + letter
    return partial_string



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    output_string = ""
    for letter in alphabet:
        if letter not in letters_guessed:
            output_string = output_string + letter
    return output_string
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Get Info about Secret Word
    number_letters = len(secret_word) + 1
    print("Welcome to Hangman")
    print("Your secret word has", number_letters, "to find.")
    guesses_remaining = 6
    warnings_remaining= 3
    letters_guessed = []
    is_unsolved = True
    vowels = ['a', 'e', 'i', 'o', 'u']
    while (guesses_remaining > 0) and (is_unsolved == True):
        print("You have",guesses_remaining,"guesses remaining.\n")
        print("Your available letters are:")
        print(get_available_letters(letters_guessed))
        guess = input("What letter do you guess? ")
        if str.isalpha(guess) == False and warnings_remaining > 0:
            print("Please only input letters. Here's a warning")
            warnings_remaining -= 1
            continue
        if str.isalpha(guess) == False and warnings_remaining <= 0:
            print("Please only input letters You lose a guess.")
        guess = str.lower(guess)
        if guess in letters_guessed:
            # print already guessed
            print("You already guessed", guess)
            if warnings_remaining > 0:
                print("That's a warning. You have ", warnings_remaining, "remaining.")
        else:
            letters_guessed.append(guess)
        if guess not in secret_word and guess not in vowels:
            print("\nOops!", guess, "is not in the secret word.")
            warnings_remaining = 3
            guesses_remaining -= 1
        elif guess not in secret_word and guess in vowels:
            print("\nOops!", guess, "is not in the secret word. Vowels are worth double.")
            warnings_remaining = 3
            guesses_remaining -= 2
        if is_word_guessed(secret_word, letters_guessed):
            is_unsolved = False
            print("---------------")
            score = 0
            unique_letters_secret_word = []
            for letter in secret_word:
                if letter not in unique_letters_secret_word:
                    score += 1
                    unique_letters_secret_word.append(letter)
            score = score * guesses_remaining
            print("Congratulations, you won! Your score is", score)
        else:
            warnings_remaining = 3
            print(get_guessed_word(secret_word, letters_guessed))
            print("----------------")
    print("The secret word was", secret_word,"Thanks for playing")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    my_word = my_word.strip()
    my_word = my_word.replace(" ","") # get rid of internal spaces
    lengthGuess = len(my_word)
    lengthOther = len(other_word)
    if lengthGuess != lengthOther:
        return False
    for i in range(lengthGuess):
        if my_word[i] == "_":
            continue
        else:
            if my_word[i] != other_word[i]:
                return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word)
        pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    number_letters = len(secret_word) + 1
    print("Welcome to Hangman")
    print("Your secret word has", number_letters, "to find.")
    guesses_remaining = 6
    warnings_remaining= 3
    letters_guessed = []
    is_unsolved = True
    vowels = ['a', 'e', 'i', 'o', 'u']
    while (guesses_remaining > 0) and (is_unsolved == True):
        print("You have",guesses_remaining,"guesses remaining.\n")
        print("Your available letters are:")
        print(get_available_letters(letters_guessed))
        guess = input("What letter do you guess? ")
        valid_guesses = 'abcdefghijklmnopqrstuvwxyz*'
        guess = str.lower(guess)
        guess = str.strip(guess)
        if guess in valid_guesses == False and warnings_remaining > 0:
            print("Please only input letters. Here's a warning")
            warnings_remaining -= 1
            continue
        if guess in valid_guesses == False and warnings_remaining <= 0:
            print("Please only input letters You lose a guess.")
        if guess == '*': 
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            # print already guessed
            print("You already guessed", guess)
            if warnings_remaining > 0:
                print("That's a warning. You have ", warnings_remaining, "remaining.")
        else:
            letters_guessed.append(guess)
        if guess not in secret_word and guess not in vowels:
            print("\nOops!", guess, "is not in the secret word.")
            warnings_remaining = 3
            guesses_remaining -= 1
        elif guess not in secret_word and guess in vowels:
            print("\nOops!", guess, "is not in the secret word. Vowels are worth double.")
            warnings_remaining = 3
            guesses_remaining -= 2
        if is_word_guessed(secret_word, letters_guessed):
            is_unsolved = False
            print("---------------")
            score = 0
            unique_letters_secret_word = []
            for letter in secret_word:
                if letter not in unique_letters_secret_word:
                    score += 1
                    unique_letters_secret_word.append(letter)
            score = score * guesses_remaining
            print("Congratulations, you won! Your score is", score)
        else:
            warnings_remaining = 3
            print(get_guessed_word(secret_word, letters_guessed))
            print("----------------")
    print("The secret word was", secret_word,"Thanks for playing")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
