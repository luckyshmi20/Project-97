import random
chances = 5
number = random.randint(1,10)
guess=input('Enter a number')
while chances < 5:
    input('Enter your guess:')
    if guess == number:
        print('Congrats!!!! YOU WONNN')
        break
    if guess > number:
        print('guess is too high, try again')
        break
    if guess < number:
        print('guess is too low, try again')
        break
    if chances == 0:
        print('You lost :( The number is: ' + number)
        break
    