# a random number guessing game
#importing random module
import random

#generating answer for one particular session
ans = random.randrange(6)
num = ''
tries = 0

#the game
while ans != num:
    if tries < 3:
        num = int(input('guess the number (hint: 0-5): '))
        if num == ans:
            print('congrats you guessed it bro!!')
            exit()
        else:
            print('try again')
            tries += 1
    else:
        print('out tries!!')
        exit()

