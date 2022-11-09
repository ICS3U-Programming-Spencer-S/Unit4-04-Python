#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Created: Nov 8, 2022
# Guessing game program with a loop used when the incorrect answer is picked


import random

# Creates our needed random number
random_number = random_number = random.randint(0, 9)


def main():

    # Spacer
    print("")
    # Tries to get the user's number as an integer.
    try:
        user_input = int(input("Enter a number between 0-9: "))
    # Exception used when the user failed to enter a number.
    except ValueError:
        input("Your input is invalid, use numbers 0-9 only: ")
    # If statement in case of negative inputs.
    if user_input < 0 and user_input < 9:
        print("Your input is invalid. Use numbers 0-9: ")

    else:
        # If user guess is correct
        while random_number == user_input:
            print("You guessed the correct number.")
            break
        # If user guess is incorrect, retry will start
        if user_input != random_number:
            print("Input {}, is not correct. Try again.".format(user_input))
            main()


if __name__ == "__main__":
    main()
