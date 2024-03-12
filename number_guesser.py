# a random number guessing game
import random

ans = random.randrange(6)
num = ''
tries = 0

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

