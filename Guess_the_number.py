# Guess the number game
# Create a random Integer between the bounds: random.randint(lower_bound, upper_bound)
# Ask user for the range of upper and lower bound
# Attempt Counter - After Correct Guesses are done
# Hints : Using if-elif-else block (Higher or Lower)
# Certain Number of Attempts

import random

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

def max_attempts():
    try:
        attempts = int(input("How many attempts do you think you can clear it in?😏 "))
        return attempts
    except ValueError:
        print("Invalid input. Please enter a whole number.")



def get_range():
    while True:
        lower = get_valid_input("Enter Lower Bound: ")
        upper = get_valid_input("Enter Upper Bound: ")
        if lower < upper:
            return lower, upper
        else:
            print("Lower bound must be Higher then Upper! Try Again")


def play_guess_game():

    print("Welcome to the Game of Guesses :)")

    while True:
        lower, upper = get_range()
        attempts_left = max_attempts()
        guess_number = random.randint(lower, upper)
        counter = 0
        print(f"I've picked a number between {lower} and {upper}. You've {attempts_left} attempts left")

        while True:
            if counter >= attempts_left:
                print("-" * 45)
                print(f"Boo lol! No attempts left for you! The Secret Number was '{guess_number}'")
                print("-" * 45)
                break

            try:
                user_input = int(input("Guess the number:"))
            except ValueError:
                print("Provide Integer input only")
                continue

            if user_input == guess_number:
                print("-" * 45)
                print("Nice job!")
                counter += 1
                break
            elif user_input < guess_number:
                print("Wrong! Hint: Guess a Higher Number!!")
                counter += 1
            elif user_input > guess_number:
                print("Wrong! Hint: Try a smaller number >_<")
                counter += 1
        print(f"Your total attempts: {counter}")
        try:
            continue_playing = input("Do you wish to continue (Y): ").strip().lower()
        except Exception as e:
            print(f"Something went wrong: {e}")
            break

        if continue_playing != 'y':
            print("Thanks for playing")
            break

if __name__ == "__main__":
    play_guess_game()




