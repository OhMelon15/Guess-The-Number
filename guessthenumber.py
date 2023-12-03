# Credit belong to FreeCodeCamp
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:  
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again, too low")
        elif guess > random_number:
            print("Sorry guess again, too high")
        elif guess >= random_number:
            print(f"Yay, you win the game, the correct number is {random_number}!")

guess(10)