while True:
    try:
        fraction = input("Enter fuel level as a fraction (X/Y): ")
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        if y == 0 or x > y:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please try again.")

percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")