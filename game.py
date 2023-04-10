import random

while True:
    level_str = input("Enter a level (a positive integer): ")
    try:
        level = int(level_str)
        if level <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

number = random.randint(1, level)

while True:
    guess_str = input("Guess a number between 1 and {}: ".format(level))
    try:
        guess = int(guess_str)
        if guess <= 0:
            print("Invalid input. Please enter a positive integer.")
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")