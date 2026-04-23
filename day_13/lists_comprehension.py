"""Day 13: 30 Days of python programming"""

# Level 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [num for num in numbers if num <= 0]
print("Negative numbers:", negative_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in list_of_lists for num in sublist]
print("Flattened list:", flattened_list)
