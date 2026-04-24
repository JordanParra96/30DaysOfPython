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
