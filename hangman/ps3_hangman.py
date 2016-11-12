# Hangman game

import random


WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    t = True
    for x in secretWord:
        if x not in lettersGuessed:
            t = False
            break
    return t


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    x = ""
    for a in secretWord:
        if a in lettersGuessed:
            x += a + " "
        else:
            x += "_ "
    return x


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = ""
    for a in alphabet:
        if a not in lettersGuessed:
            x += a
    return x


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    lettersGuessed=[]
    mistakesMade=0
    while not isWordGuessed(secretWord, lettersGuessed):
        if not mistakesMade<8:
            break
        print("-----------")
        print("You have "+str(8-mistakesMade)+" guesses left.")
        availableLetters=getAvailableLetters(lettersGuessed)
        print("Available Letters: "+availableLetters)
        c=input("Please guess a letter: ")
        if c[0] in lettersGuessed:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            continue
        lettersGuessed.append(c[0])
        if c[0] in secretWord:
            print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
            mistakesMade+=1
    print("-----------")
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was "+secretWord+".")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
