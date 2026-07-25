"""Arithmetic module for basic mathematical operations."""


# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    """A function that takes any number of arguments and returns the sum of all the numbers."""
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    """A function that takes two numbers and returns the difference of the two numbers."""
    return a - b


def multiple(a, b):
    """A function that takes two numbers and returns the product of the two numbers."""
    return a * b


def division(a, b):
    """A function that takes two numbers and returns the quotient of the two numbers."""
    return a / b


def remainder(a, b):
    """A function that takes two numbers and returns the remainder of the two numbers."""
    return a % b


def power(a, b):
    """Takes two numbers and returns the first number raised to the power of the second number."""
    return a**b
