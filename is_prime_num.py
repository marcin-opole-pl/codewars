"""
Checks if number is a prime number.
"""

def prime(number):
    """
    Checks prime number.
    """
    for i in range(2, int(number/2 + 1)):
        if (number % i) == 0:
            return False
    return True

print(prime(10000019))
