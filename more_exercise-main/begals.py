# import random

# def getSecretNum(numDigits):

# # Returns a string that is numDigits long, made up of unique random digits.

#   numbers = list(range(10))

#   random.shuffle(numbers)

#   secretNum = ''

#   for i in range(numDigits):

#     secretNum = (numbers[i])

#   print(secretNum)
# getSecretNum(2)

# def getClues(guess, secretNum):

# # Returns a string with the pico, fermi, None clues to the user.

#   if guess == secretNum:

#     return 'You got it!'

#   clue = []

#   for i in range(guess):

#     if guess[i] == secretNum[i]:

#       clue.append('Fermi')

#     elif guess[i] in secretNum:

#       clue.append('Pico')

#     if len(clue) == 0:

#       return 'None'

#   return ' '.join(clue)
# guess=int(input("enter the number"))
# getClues(2,8)

# def isOnlyDigits(num):

# # Returns True if num is a string made up only of digits. Otherwise returns False.

#   if num == '':

#     return False


#   for i in num:

#     if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:

#       return False
# isOnlyDigits(4)

# def playAgain():

# # This function returns True if the player wants to play again, otherwise it returns False.

#   play = input("Do you want to play again? Yes or No?") 

#   return play.lower.startswith('y')
# NUMDIGITS = 3

# MAXGUESS = 10


# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))

# print('Here are some clues:')

# print('When I say:    That means:')

# print('  Pico         One digit is correct but in the wrong position.')

# print('  Fermi        One digit is correct and in the right position.')

# print('  None       No digit is correct.')


# while True:

#     secretNum = getSecretNum(NUMDIGITS)

    # print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))

    # numGuesses = 1

    # while numGuesses <= MAXGUESS:

    #     while (numGuesses) != NUMDIGITS or not isOnlyDigits(guess):

    #         print ('Guess'+(numGuesses))

    #     guess = input("Guess Again")
    #     clue = getClues(guess, secretNum)

    # print(clue)

    # numGuesses += 1

    # if guess == secretNum:

    #   break

    # if numGuesses < MAXGUESS:
    #      print ('You ran out of guesses. The answer was ' + secretNum)

    # if not playAgain:

    #   break






from random import sample, shuffle

digits = 3
guesses = 10

print('I am thinking of a', digits, 'digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  pico         One digit is correct but in the wrong position.')
print('  fermi        One digit is correct and in the right position.')
print('  bagels       No digit is correct.')
print('There are no repeated digits in the number.')

# Create a random number.

letters = sample('0123456789', digits)

if letters[0] == '0':
    letters.reverse()

number = ''.join(letters)

print('I have thought up a number.')
print('You have', guesses, 'guesses to get it.')

counter = 1

while True:
    print('Guess #', counter)
    guess = input()

    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Create the clues.

    clues = []

    for index in range(digits):
        if guess[index] == number[index]:
            clues.append('fermi')
        elif guess[index] in number:
            clues.append('pico')

    shuffle(clues)

    if len(clues) == 0:
        print('bagels')
    else:
        print(' '.join(clues))

    counter += 1

    if guess == number:
        print('You got it!')
        break

    if counter > guesses:
        print('You ran out of guesses. The answer was', number)
        break       
            


