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


def check_season(month):
    """Determines the season based on the month."""
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    if month in ['march', 'april', 'may']:
        return 'Spring'
    if month in ['june', 'july', 'august']:
        return 'Summer'
    if month in ['september', 'october', 'november']:
        return 'Fall'
    return None


print('Season for April:', check_season('April'))


def calculate_slope(x1, y1, x2, y2):
    """Calculates the slope of a line given two points (x1, y1) and (x2, y2)."""
    if x2 - x1 == 0:
        return 'Undefined (vertical line)'
    return (y2 - y1) / (x2 - x1)


print('Slope of line through points (1, 2) and (3, 4):',
      calculate_slope(1, 2, 3, 4))


def solve_quadratic_eqn(a, b, c):
    """Solves the quadratic equation ax^2 + bx + c = 0 and returns the roots."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No real roots'
    if discriminant == 0:
        root = -b / (2*a)
        return f'One real root: {root}'

    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return f'Two real roots: {root1} and {root2}'


print('Roots of equation 2x^2 + 3x - 2 = 0:',
      solve_quadratic_eqn(2, 3, -2))


def print_list(lst):
    """Prints each item in the list on a new line."""
    for item in lst:
        print(item)


print('Print list items:')
print_list(['apple', 'banana', 'cherry'])


def reverse_list(lst):
    """Reverses the list and returns it."""
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst


print('Reverse list:', reverse_list([1, 2, 3, 4, 5]))


def capitalize_list_items(lst):
    """Capitalizes each string item in the list and returns the new list."""
    return [item.capitalize() for item in lst if isinstance(item, str)]


print('Capitalize list items:', capitalize_list_items(
    ['apple', 'banana', 'cherry']))


def add_item(lst, item):
    """Adds an item to the list."""
    lst.append(item)
    return lst


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('Add item to list:', add_item(food_stuff, 'Meat'))


def remove_item(lst, item):
    """Removes an item from the list if it exists."""
    if item in lst:
        lst.remove(item)
    else:
        print(f'Item {item} not found in the list.')
    return lst


numbers = [2, 3, 7, 9]
print('Remove item from list:', remove_item(numbers, 3))


def sum_of_numbers(*args):
    """Returns the sum of all the numbers passed as arguments."""
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f'Warning: {num} is not a number and will be ignored.')
    return total


print('Sum of numbers:', sum_of_numbers(1, 2, 3, 4, 5))


def sum_of_odds(*args):
    """Returns the sum of all the odd numbers passed as arguments."""
    total = 0
    for num in args:
        if isinstance(num, (int, float)) and num % 2 != 0:
            total += num
        else:
            print(f'Warning: {num} is not an odd number and will be ignored.')
    return total


print('Sum of odd numbers:', sum_of_odds(1, 2, 3, 4, 5))


def sum_of_evens(*args):
    """Returns the sum of all the even numbers passed as arguments."""
    total = 0
    for num in args:
        if isinstance(num, (int, float)) and num % 2 == 0:
            total += num
        else:
            print(f'Warning: {num} is not an even number and will be ignored.')
    return total


print('Sum of even numbers:', sum_of_evens(1, 2, 3, 4, 5))
