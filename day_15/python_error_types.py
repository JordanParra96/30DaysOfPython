"""Day 15: 30 Days of python programming"""

# ModuleNotFoundError - import maths
import math  # Corrected import statement

# ImportError - from string import dig
from string import digits  # Corrected import statement

print(digits)  # Corrected to print the imported 'digits' from string module

# Syntax error - print "Hello Woerld!"
print("Hello, World!")

# Name error - print(age)
AGE = 25
print(AGE)

# Index error - numbers[10]
numbers = [1, 2, 3, 4, 5]
print(numbers[4])  # Accessing the last valid index

# AttributeError - math.PI
print(math.pi)  # Corrected attribute name

# KeyError - users['county']
users = {"name": "John", "age": 30, "country": "Colombia"}
print(users["country"])  # Accessing a valid key

# TypeError - 4 + '3'
RESULT = 4 + int("3")  # Corrected to convert string to integer
print(RESULT)

# ValueError - int('12a')
print(int("12"))  # Corrected to a valid integer string
