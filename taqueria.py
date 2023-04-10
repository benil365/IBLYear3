# This is a Python program that defines a dictionary called `menu` that contains food items as keys
# and their corresponding prices as values. The program then prompts the user to enter an item from
# the menu and adds the price of the item to a running total cost. The program continues to prompt the
# user for items until the user enters an end-of-file (EOF) character, at which point the program
# exits and prints the total cost of all items entered.
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.0
while True:
    try:
        item = input("Enter an item: ").title()
        if item not in menu:
            continue
        price = menu[item]
        total_cost += price
        print(f"${total_cost:.2f}")
    except EOFError:
        break