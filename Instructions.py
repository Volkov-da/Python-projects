#!/usr/local/bin/python3.8
def is_simple_number(x):
    """
    This function checks if the given number simple or not.
    x - integer number which will be checked
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x):
    """
    Раскладывает число на множители.
    Печатает их на экран.
    x - целое положительное число.
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


def useless_function():
    """
     This function doing absolutely nothing!
     """
