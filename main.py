# Choosing a random number between 1 and 100
import random
from wsgiref.util import guess_scheme

ANSWER = random.randint(1, 100)

# Function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty level [1/2]: ").lower()
    if level == "1":
        return 10
    else:
        return 5

# Let the user guess a number

def check_guess(guess, answer):
    if guess > answer:
        print("Too high!")
        return False
    elif guess < answer:
        print("Too low!")
        return False
    else:
        print(f"You got it! The answer is {answer}.")
        return True

# Function to check users' guess against actual answer

def game():
    print("Welcome to the Numer Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = set_difficulty()
    guessed_correctly = False

    while turns > 0 and not guessed_correctly:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        guessed_correctly = check_guess(guess, ANSWER)
        if not guessed_correctly:
            turns -= 1
            if turns == 0:
                print("You lose!")
            else:
                print("Try again!")

#Track the number of turns and reduce by 1 if they rget wrong

game()