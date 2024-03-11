# Problem Set 4C
# Name: Caleb Bibb
# Collaborators:
# Time Spent: 10 hours

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        new_list = self.valid_words.copy()
        return new_list
             
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower_vowels = "aeiou"
        lower_letters = string.ascii_lowercase
        this_dict = {}
        for i in range(len(vowels_permutation)):
            lower_vowel = lower_vowels[i]
            upper_vowel = lower_vowel.capitalize()
            this_dict[lower_vowel] = vowels_permutation[i].lower()
            this_dict[upper_vowel] = vowels_permutation[i].capitalize()
        for letter in lower_letters:
            if letter not in this_dict.keys():
                capital = letter.capitalize()
                this_dict[letter] = letter
                this_dict[capital] = capital
        return this_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        message = self.get_message_text()
        output = ""
        symbols = [" ", "!", ".", ",", "?", "'"]
        for letter in message:
            if letter in symbols:
                output += letter
            else:
                temp = transpose_dict[letter]
                output = output + temp

        return output
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # Define Vowels and get permutations
        vowels = "aeiou"
        permutations = get_permutations(vowels)

        # Store best permutation
        best_permutation = ""
        # Store best english word score
        english_word_high_score = 0
        # Get valid word list
        temp_word_list = self.get_valid_words()
        # For each permutation:
        for permutation in permutations:
            # Build dictionary using looped permutation
            dictionary = self.build_transpose_dict(permutation)
            # Apply dictionary to message
            temp_message = self.apply_transpose(dictionary)
            # split it into individual "words"
            temp_message = temp_message.split()
            
            # Looped number of english words
            english_score = 0
            
            #For each word in split message:
            for word in temp_message:
                # Change to lower case
                word = word.lower()
                if not word.isalpha():
                    output = ""
                    for letter in word:
                        if letter.isalpha():
                            output = output + letter
                    word = output

                # Check word for english
                if word in temp_word_list:
                    english_score += 1
    
            # If theres a high score for english:
            if english_score > english_word_high_score:
                # Store the permutation and the high english score
                best_permutation = permutation
                english_word_high_score = english_score
        # If high score is more than 1:
        if english_word_high_score > 1:
            # return the message
            best_dictionary = self.build_transpose_dict(best_permutation)
            best_message = self.apply_transpose(best_dictionary)
            print(english_word_high_score)
            return best_message
        # If no english words are found at all:
        else:
            #return the original string
            return self.get_message_text()

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
        # Test 1
    message1 = SubMessage("This Works!")
    permutation1 = "iouae"
    enc_dict1 = message1.build_transpose_dict(permutation1)  
    print("Original message:", message1.get_message_text(), "Permutation:", permutation1)
    print("Expected encryption:", "Thus Warks!")
    print("Actual encryption:", message1.apply_transpose(enc_dict1))
    enc_message1 = EncryptedSubMessage(message1.apply_transpose(enc_dict1))
    print("Decrypted Message:", enc_message1.decrypt_message())    
    # Test 2
    message2 = SubMessage("Hmmm... Maybe?")
    permutation2 = "uioea"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "Hmmm... Muybi?")
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    