"""Day 13: 30 Days of python programming"""

# Level 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [num for num in numbers if num <= 0]
print("Negative numbers:", negative_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in list_of_lists for num in sublist]
print("Flattened list:", flattened_list)

list_of_tuples = [(num, 1, num, num**2, num**3, num**4, num**5) for num in range(11)]
print("List of tuples:", list_of_tuples)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

formatted_countries = [
    [(country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper())]
    for country in countries
]
print("Formatted countries:", formatted_countries)

list_of_dictioanries = [
    {"country": country[0][0].upper(), "city": country[0][1].upper()}
    for country in countries
]
print("List of dictionaries:", list_of_dictioanries)
