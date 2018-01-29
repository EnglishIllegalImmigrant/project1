# Import modules
import random

# Define variables
computer_number = random.randint(1, 100)
guessed = 0
wrong = 0

# Repeat this block of code until user guesses correctly
while(guessed == 0):
    user_number = int(input('Guess a number between 1-100: '))
    if(user_number == computer_number):
        print('Congratulations! You won a small loan of a billion dollars!')
        guessed = 1
    elif(user_number > computer_number):
        print('You guessed higher.')
        wrong += 1
        print('You\'ve guessed incorrectly', wrong, 'times.')
    elif(user_number < computer_number):
        print('You guessed lower.')
        wrong += 1
        print('You\'ve guessed incorrectly', wrong, 'times.')