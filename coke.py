def get_coin_value(coin):
    """
    The function returns the value of a coin if it is 25, 10, or 5, and returns 0 otherwise.
    
    :param coin: an integer representing the value of a coin in cents (e.g. 25 for a quarter, 10 for a
    dime, 5 for a nickel)
    :return: The function `get_coin_value` returns the value of the coin if it is a quarter (25), dime
    (10), or nickel (5). If the coin is not one of these values, it returns 0.
    """
    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        return 0

total = 0
# This code is simulating a vending machine that accepts coins of 25, 10, or 5 cents and dispenses an
# item that costs 50 cents. The `while` loop keeps prompting the user to insert a coin until the total
# amount inserted reaches 50 cents. The `get_coin_value` function checks if the coin inserted is valid
# and returns its value if it is valid. If the coin is not valid, the program prints an error message
# and continues the loop. The program keeps track of the total amount inserted and displays the amount
# due after each coin is inserted. Once the total amount inserted reaches 50 cents, the program
# calculates the change owed and displays it.
while total < 50:
    coin = int(input("Insert a coin (25, 10, or 5): "))
    coin_value = get_coin_value(coin)
    if coin_value == 0:
        print("Invalid coin.")
        continue
    total += coin_value
    print(f"Amount due: {50 - total} cents.")
    
change = total - 50
print(f"Change owed: {change} cents.")