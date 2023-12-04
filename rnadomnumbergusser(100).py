import random

num = random.randint(1, 100)#you can change the range of the number in this
guess = None

while guess != num:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")
