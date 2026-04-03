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

# Level 2


def evens_and_odds(n):
    """Returns the count of even and odd numbers from 0 to n."""
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'Number of evens: {evens}, Number of odds: {odds}'


print('Evens and odds from 0 to 100:', evens_and_odds(100))


def factorial(n):
    """Returns the factorial of a number."""
    if n < 0:
        return 'Factorial is not defined for negative numbers.'
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print('Factorial of 5:', factorial(5))


def is_empty(param):
    """Checks if the given parameter is empty."""
    if param is None:
        return True
    if isinstance(param, (str, list, tuple, dict, set)):
        return len(param) == 0
    return False


print('Is empty string:', is_empty(''))
print('Is empty list:', is_empty([]))
print('Is empty dict:', is_empty({}))


def calculate_mean(*args):
    """Returns the mean of the numbers passed as arguments."""
    total = 0
    count = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
            count += 1
        else:
            print(f'Warning: {num} is not a number and will be ignored.')
    return total / count if count > 0 else 'No valid numbers provided.'


print('Mean of numbers:', calculate_mean(1, 2, 3, 4, 5))


def calculate_median(*args):
    """Returns the median of the numbers passed as arguments."""
    for num in args:
        if not isinstance(num, (int, float)):
            print(f'Warning: {num} is not a number and will be ignored.')
        numbers.sort()
        n = len(numbers)
        mid = n // 2

    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]


print('Median of numbers:', calculate_median(1, 2, 3, 4, 5))


def calculate_mode(*args):
    """Returns the mode of the numbers passed as arguments."""
    frequency = {}
    for num in args:
        if isinstance(num, (int, float)):
            frequency[num] = frequency.get(num, 0) + 1
        else:
            print(f'Warning: {num} is not a number and will be ignored.')

    mode = max(frequency, key=frequency.get)
    return mode


print('Mode of numbers:', calculate_mode(1, 2, 2, 3, 4, 5))


def calculate_range(*args):
    """Returns the range of the numbers passed as arguments."""
    for num in args:
        if not isinstance(num, (int, float)):
            print(f'Warning: {num} is not a number and will be ignored.')

    return max(numbers) - min(numbers)


print('Range of numbers:', calculate_range(1, 2, 3, 4, 5))


def calculate_variance(*args):
    """Returns the variance of the numbers passed as arguments."""
    for num in args:
        if not isinstance(num, (int, float)):
            print(f'Warning: {num} is not a number and will be ignored.')

    mean = calculate_mean(*numbers)
    variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)
    return variance


print('Variance of numbers:', calculate_variance(1, 2, 3, 4, 5))


def calculate_std(*args):
    """Returns the standard deviation of the numbers passed as arguments."""
    variance = calculate_variance(*args)
    if isinstance(variance, str):
        return variance
    return variance ** 0.5


print('Standard deviation of numbers:', calculate_std(1, 2, 3, 4, 5))
