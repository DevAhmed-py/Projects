#Number Guessing Game

from random import randint

val = randint(0,100)

while True:

    guess = int(input('\nPlease enter a number: '))

    if guess == val:
        break

    elif guess < val:
        print('\nYour guess is too low')

    else:
        print('\nYour guess is too high')


print('\nYou guessed the number correctly: ',guess)
