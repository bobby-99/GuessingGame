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

def max_attempts():
    while True:
        print('''Attempt Category:
        1. Easy (10 attempts)
        2. Mediocre (5 attempts)
        3. Hard (3 attempts)
        or Custom Input''')
        try:
            difficulty_level = int(input("Select Difficulty Option (1/2/3/Custom Input) : "))
            if difficulty_level in (1,2,3):
                if difficulty_level == 1:
                    attempts = 10
                    return attempts
                elif difficulty_level == 2:
                    attempts = 5
                    return attempts
                else:
                    attempts = 3
                    return attempts
            else:
                try:
                    attempts = int(input("How many attempts do you think you can clear it in?😏 "))
                    return attempts
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_range():
    while True:
        lower = get_valid_input("Enter Lower Bound: ")
        upper = get_valid_input("Enter Upper Bound: ")
        if lower < upper:
            return lower, upper
        else:
            print("Lower bound must be Lower then Upper! Try Again")


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

            counter += 1

            if user_input == guess_number:
                print("-" * 45)
                print("Correct Guess! Nice job!")
                break
            elif user_input < guess_number:
                print("Wrong! Hint: Guess a Higher Number!!")
            else:
                print("Wrong! Hint: Try a smaller number >_<")
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




