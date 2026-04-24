"""Day 14: 30 Days of python programming"""

from functools import reduce

# level 1
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

is_even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", is_even)

total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)


def uppercase_decorator(func):
    """decorator function to convert the result of a function to uppercase"""

    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@uppercase_decorator
def greet():
    """This function returns a greeting message."""
    return "Hello, World!"


print("Decorator example:", greet())


def add_one():
    """This function adds 1 to a number."""

    def inner(a):
        return a + 1

    return inner


add_one_func = add_one()
print("Closure example:", add_one_func(5))


def square(x):
    """This function returns the square of a number."""
    return x**2


squared_numbers = list(map(square, numbers))
print("Squared numbers using defined function:", squared_numbers)


def is_even_func(x):
    """This function checks if a number is even."""
    return x % 2 == 0


is_even = list(filter(is_even_func, numbers))
print("Even numbers using defined function:", is_even)


def add(x, y):
    """This function adds two numbers."""
    return x + y


total = reduce(add, numbers)
print("Sum of numbers using defined function:", total)

for country in countries:
    print(f"{country}")

for name in names:
    print(f"{name}")

for number in numbers:
    print(f"{number}")

# level 2
print("Countries in uppercase: ", list(map(lambda x: x.upper(), countries)))

print("Squared numbers: ", list(map(lambda x: x**2, numbers)))

print("Names in uppercase: ", list(map(lambda x: x.upper(), names)))

print("countries that contain 'land': ", list(filter(lambda x: "land" in x, countries)))

print(
    "countries that have six character: ",
    list(filter(lambda x: len(x) == 6, countries)),
)

print(
    "Countries that contain six letters and more: ",
    list(filter(lambda x: len(x) >= 6, countries)),
)
