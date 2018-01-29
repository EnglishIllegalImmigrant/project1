# Import modules
import random

# Define variables
computer_number = random.randint(1, 100)
playGame = True
wrong = 0

# Repeat this block of code until user does not want to play
while(playGame):
    user_number = int(input('Guess a number between 1-100: '))
    if(user_number == computer_number):
        print('Congratulations! You won a small loan of a billion dollars!')
        answer = input('Do you want to play again? ')
        if(answer == 'Yes' or 'yes'):
            playGame = True
        elif(answer == 'No' or 'no'):
            playGame = False
        else:
            print('Invalid response. Default is "no".')
            playGame = False
    elif(user_number > computer_number):
        print('You guessed higher.')
        wrong += 1
        print('You\'ve guessed incorrectly', wrong, 'times.')
    elif(user_number < computer_number):
        print('You guessed lower.')
        wrong += 1
        print('You\'ve guessed incorrectly', wrong, 'times.')