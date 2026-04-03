''' Day 11: 30 Days of python programming '''

# Level 1


def add_two_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 + num2


print('Add two numbers:', add_two_numbers(3, 5))


def area_of_circle(radius):
    """Calculates the area of a circle given its radius."""
    pi = 3.14
    return pi * radius ** 2


print('Area of circle with radius 5:', area_of_circle(5))


def add_all_nums(*args):
    """Adds all the numbers passed as arguments and returns the result."""
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f'Warning: {num} is not a number and will be ignored.')
    return total


print('Add all numbers:', add_all_nums(1, 2, 3, 4, 5))


def convert_celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


print('Convert 25°C to Fahrenheit:', convert_celsius_to_fahrenheit(25))
