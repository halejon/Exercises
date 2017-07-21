# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def input_guess():
    return raw_input("Please guess a letter: ")


def check_guess(word, guess):
    """
    Function to check if a guess is in the word
    :param word:the word we are trying to guess
    :param guess: the current letter we are guessing
    :return: returns the letter if in the word and False otherwiase
    """
    if guess in word:
        return guess
    else:
        return False

def update_solution(guess, word, solution):
    """

    :param guess: the current guess
    :param word: the word we are trying to guess
    :param solution: the letters we have guessed correctly so far and _ in the positions for letters we have yet to guess
    correctly
    :return: an updated solution with the the current guess in place of '_' respective to the position of the guess in
    the word
    """
    updated_solution = []
    for x, y in zip(list(word), list(solution)):
        if guess == x:
            updated_solution.append(guess)
        else:
            updated_solution.append(y)

    return updated_solution

word = choose_word(wordlist)
rem_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

print word

word_len = len(word)
rem_guess = word_len
solution = "_" * word_len

print "Welcome to the game, Hangman!"
print "I am thinking of a word that is %d letters long." % (word_len)


while rem_guess > 0:
    print "-" * 8
    print "You have %d guesses left" % (rem_guess)
    print "Available letters: " + ''.join(rem_letters)

    cur_guess = input_guess().lower()

    #check if our guess is in the remaining letters
    if cur_guess in rem_letters:
        rem_letters.remove(cur_guess)
        #check if our guess is in the target word
        if check_guess(word, cur_guess):
            solution = ''.join(update_solution(cur_guess, word, solution))
            print "Good guess: ", solution
        else:
            #decrementing function (how we know our while loop will eventually end)
            rem_guess = rem_guess - 1
            print "Oops! That letter is not in my word: ", solution
    else:
        print "please enter a valid guess"

    if solution == word:
        print "Congratulations, you won!"
        break

if rem_guess == 0:
    print "SUBOPTIMAL PLAY"
