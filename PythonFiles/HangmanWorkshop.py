import random

HANGMAN = [
'''







=======
''',
'''

     +
     |
     |
     |
     |
     |
=======
''',
'''

 +---+
     |
     |
     |
     |
     |
=======
''',
'''

 +---+ 
 0   |
     |
     |
     |
     |
=======
''',
'''

 +---+
 0   |
 |   |
     |
     |
     |
=======
''',  
'''

 +---+
 0   |
/|   |
     |
     |
     |
=======
''',
'''

 +---+
 0   |
/|\  |
     |
     |
     |
=======
''', 
'''

 +---+
 0   |
/|\  |
/    |
     |
     |
=======
''',
'''

 +---+
 0   |
/|\  |
/ \  |
     |
     |
=======
''',
'''

 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=======

* * * G A M E O V E R * * *

''' 
]

WORDS = ['Brisbane', 'Caloundra', 'Nambour', 'Gympie', 'Tiaro', 'Maryborough',
'Childers', 'Bundaberg', 'Gladstone', 'Rockhampton', 'Mackay', 'Townsville', 
'Innisfail', 'Cairns', 'Atherton', 'Charleville', 'Longreach']



'''
    This function chooses a random integer value that will be
    the index location for the wordlist parameter.

    Parameter wordList: a list of words for the game.
    Returns: a specific random word in the word list.

    Hints: 
    The len function is a useful function to find the length of a given
    object such as a list or string.

    Remember that lists are indexed from zero. Therefore the index of an
    item in a list is the length of the list - 1.
'''
def selectWord(wordList):
    pass


'''
    This function allows the player to input a single alphabetical character.
    This function loops through checks to ensure it meets criteria of:
        single character
        alphabetical character
        not already guessed

    Parameter guessedLetters: a list of characters that the player has already
    guessed. 
    Returns: a single alphabetical character that is the player's guess.

    Hints:
    A while loop is useful to ensure the correct input is provided.
    Applying some checks, and only when they pass, the character is returned
    is a good way to exit this loop.

    The input() function is your way to allow a user to input text to
    the program. 

    Python recognises that uppercase and lowercase characters are different.
    It is possible to make a character uppercase or lowercase on input.
    Review the upper() or lower() string functions to achieve this.
'''
def getLetter(guessedLetters):
    pass




'''
    This function draws the current Hangman stage to the shell window.

    Parameter incorrectGuesses: the list of incorrectly guessed characters.
    Return: None

    Hints:
    Each hangman 'stage' is a unique list object.
    One option is to print the specific list object based on the length of the
    incorrectly guessed character list.
    Eg: a zero length character list will print the zero-th index on the
    HANGMAN list while having two incorrect guessed will print the second
    stage (index) of the list.
'''
def displayHangmanStage(incorrectGuesses):
    pass


'''
    This function draws to the shell window the mix of guessed and
    unguessed characters.
    The guessed characters are the letter characters in the correct place.
    The unguessed characters are represented by an underscore character.
    For legibility, empty spaces are placed on either side of each character - 
    eg: ' _ ' ' A ' ' _ ' ' T ' 

    Parameter gameWord: the gameword chosen to be solved for this current game.
    Parameter correctLetter: the populated list of correctly guessed letters.
    Return: None

    Hints:
    Think about iterating through the gameword and using some logic
    (if statements) to decide if each character has been correctly guessed.
    If not, have that character represented as the underscore
    character ' _ ' like so.

    To stop print from creating a new line, you can add a parameter in the
    print function like so:
    print('This will print on a line', end = ' ')
    print('This will print on the same line as above', end = ' ')
'''
def displayWordAttempt(gameWord, correctLetter):
    pass

'''
    This function runs when a game is won or lost, prompting a player if they
    want to play again.

    Parameter: There are no parameters for this function
    Return: A boolean value (True or False)

    Hints:
    The game operates on a while loop. If endGame is false, then the while loop continues
    ie: while endGame == False.
    If the endGame is true, then the while loop breaks and the program
    terminates.

    It is an idea to prompt the player if they want to play again.
    One way is for them to input into the console Yes or No, and a decision
    from there (if statement) to return true or false.
'''
def playAgain():
    pass





#-----------------------------------------------------------------------------#
#                                                                             #
#                                  Main Code                                  #
#                                                                             #
#-----------------------------------------------------------------------------#

'''
The following code does not need to be edited.
The purpose of this workshop activity is to develop the problem solving
skills and apply the knowledge of Python programming language to complete the
functions above.

A full worked solution will be provided at the completion of the workshop.

Some additional ideas to extend on this program include:

    Setting up a Graphical User Interface to present a more aesthetically
    pleasing program to interact with. Refer to TKinter resources:
        https://www.tutorialspoint.com/python/python_gui_programming.htm

    Replacing the ASCII art 'Hangman' with Turtle Graphics. Develop a series
    of functions that are called based on the number of incorrect guesses
    to draw your own incorrect guesses onto the Turtle canvas.
        https://docs.python.org/3/library/turtle.html

    Use a different data structure to maintain the list of unknown words.
    Consider a dictionary such that the key is a word category and the value
    is a random choice from a list of words pertaining to that category.
        https://docs.python.org/3/tutorial/datastructures.html#dictionaries

    Create your own database to track your wins and losses, and any other
    pieces of data you'd like to keep. This can be achieved with the SQL
    libraries.
        https://docs.python.org/3.10/library/sqlite3.html
        
'''

#Initialise the end game variable state. If endGame set to True, program
#will end.
endGame = False

#Main program loop
while endGame == False:

    print('WELCOME TO HANGMAN\n\n')

    #Initialise variables on new game start.
    #Each new game is a new iteration through this while loop.
    wordAttempt = selectWord(WORDS).upper()
    incorrectLetterList = []
    correctLetterList = []

    characterSet = set(wordAttempt)

    #The game loop. 
    while True:

        #These two lines will print the current game state to the
        #shell window.
        displayWordAttempt(wordAttempt, correctLetterList)
        displayHangmanStage(incorrectLetterList)

        #This line will prompt the user for a character input
        #and assign to variable newGuess.
        newGuess = getLetter(incorrectLetterList + correctLetterList)

        #This decision tree adds the recently input character into the
        #appropriate list. 
        if newGuess in wordAttempt:
            correctLetterList.append(newGuess)
        else:
            incorrectLetterList.append(newGuess)

        #If this condition is true, the game will terminate (break).
        if len(characterSet) == len(correctLetterList):
            displayHangmanStage(incorrectLetterList)
            displayWordAttempt(wordAttempt, correctLetterList)
            print('\n* * * * * * * * * *')
            print('*                 *')
            print('*     YOU WON     *')
            print('*                 *')
            print('* * * * * * * * * *')
            break

        #If this condition is true, the game will terminate (break).
        if  len(incorrectLetterList) >= len(HANGMAN) - 1:
            displayHangmanStage(incorrectLetterList)
            displayWordAttempt(wordAttempt, correctLetterList)
            print(f'\nThe correct word was: \n{wordAttempt}')
            break

        #Neither of the if statements true? The while loop will cycle again.
        

    #Let player decide if program should terminate.
    #If playAgain function returns True, program will terminate.
    endGame = playAgain()

