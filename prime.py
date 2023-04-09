

def is_prime(n):
    """
    The function checks if a number is prime and prints all prime numbers between 1 and 150.
    
    :param n: The input number to check if it is prime or not
    :return: The code is printing all prime numbers between 1 and 150.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(1, 151):
 if is_prime (i):
    print(i)