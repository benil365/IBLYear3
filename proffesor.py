import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        answer = None
        for j in range(3):
            answer = input(f"{x} + {y} = ")
            try:
                answer = int(answer)
                if answer == x + y:
                    score += 1
                    print("Correct!")
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        if answer != x + y:
            print(f"The correct answer is {x+y}")
    print(f"Your score is {score} out of 10")


def get_level():
    while True:
        level = input("Choose a level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)


def generate_integer(level):
    if level == 1:
        digits = 1
    elif level == 2:
        digits = 2
    elif level == 3:
        digits = 3
    else:
        raise ValueError("Invalid level")
    x = random.randint(0, 10 ** digits - 1)
    y = random.randint(0, 10 ** digits - 1)
    return x, y


if __name__ == "__main__":
    main()