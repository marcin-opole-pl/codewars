"""
Armstrong number checker.
"""

def is_armstrong(number)->bool:
    """
    Takes numer and checks if it is an Armstrong number.
    Rerutns Bool.
    """
    # Check lenght of number
    power = len(str(number))
    # Calculate sum of powers
    sum_of_powers = 0
    for num in str(number):
        sum_of_powers += pow(int(num), power)
    return sum_of_powers == int(number)


print(is_armstrong(407))
