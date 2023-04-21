def convert(fraction):
    x, y = fraction.split('/')
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError('Invalid input: X and Y must be integers')
    if y == 0:
        raise ZeroDivisionError('Invalid input: Y cannot be zero')
    if x > y:
        raise ValueError('Invalid input: X cannot be greater than Y')
    percentage = round(x / y * 100)
    return min(max(0, percentage), 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


def main():
    fraction = input('Enter the fuel level as a fraction (X/Y): ')
    try:
        percentage = convert(fraction)
        print(f'The fuel gauge reads: {gauge(percentage)}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error: {e}')
"""
    The function takes a fraction as input, validates it, converts it to a percentage, and returns the
    percentage rounded to the nearest integer between 0 and 100.
    
    :param fraction: The input fraction as a string in the format "X/Y", where X and Y are integers
    :return: a percentage value (an integer between 0 and 100) that represents the fraction passed as an
    argument. If the fraction is invalid (e.g. X and Y are not integers, Y is zero, or X is greater than
    Y), the function raises an appropriate error.
    """
def main():
    fraction = input('Enter the fuel level as a fraction (X/Y): ')
    try:
        percentage = convert(fraction)
        print(f'The fuel gauge reads: {gauge(percentage)}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error: {e}')
def convert(fraction):
   
    x, y = fraction.split('/')
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError('Invalid input: X and Y must be integers')
    if y == 0:
        raise ZeroDivisionError('Invalid input: Y cannot be zero')
    if x > y:
        raise ValueError('Invalid input: X cannot be greater than Y')
    percentage = round(x / y * 100)
    return min(max(0, percentage), 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
         return f'{percentage}%'