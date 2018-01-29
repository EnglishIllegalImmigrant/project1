# Import modules
import random

# Define variables
computer_number = random.randint(1, 100)
tries = 3

# While user has tries left, repeat this block of code
while(tries != 0):
    user_number = int(input('Guess a number between 1-100: '))
    if(user_number == computer_number):
        print('Congratulations! You won a small loan of a billion dollars!')
        tries = 0
    elif(user_number > computer_number):
        print('You guessed higher.')
        tries = tries - 1
        print('You have', tries, 'tries left.')
    elif(user_number < computer_number):
        print('You guessed lower.')
        tries = tries - 1
        print('You have', tries, 'tries left.')
