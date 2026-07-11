"""Day 17: 30 Days of python programming"""

# Example
try:
    name = input("Enter your name:")
    year_born = input("Year you born:")
    age = 2019 - int(year_born)
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occur")
except ValueError:
    print("Value error occur")
except ZeroDivisionError:
    print("zero division error occur")
else:
    print("I usually run with the try block")
finally:
    print("I alway run.")


# Unpacking exmaple
def sum_of_five_nums(a, b, c, d, e):
    """Calculate the sum of five numbers."""
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# Unpacking example with lists
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  #  1 [2, 3, 4, 5, 6] 7


# Unpacking example with dictionaries
def unpacking_person_info(name_1, country, city, age_1):
    """Return a formatted string describing a person's location and age.

    Args:
        name_1 (str): Person's name.
        country (str): Country where the person lives.
        city (str): City where the person lives.
        age_1 (int): Person's age.

    Returns:
        str: Formatted description.
    """
    return f"{name_1} lives in {country}, {city}. He is {age_1} year old."


dct = {"name_1": "Asabeneh", "country": "Finland", "city": "Helsinki", "age_1": 250}
print(
    unpacking_person_info(**dct)
)  # Asabeneh lives in Finland, Helsinki. He is 250 years old.


# Packing example with lists
def sum_all(*args):
    """Calculate the sum of all arguments passed to the function.

    Args:
        *args: Variable length argument list of numbers.

    Returns:
        int: The sum of all arguments.
    """
    s = 0
    for y in args:
        s += y
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# Packing example with dictionaries
def packing_person_info(**kwargs):
    """Print keyword arguments and return them as a dictionary.

    Args:
        **kwargs: Arbitrary keyword arguments.

    Returns:
        dict: The passed keyword arguments.
    """
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    return kwargs


print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

# Spreading example
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ["Finland", "Sweden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Enumerate example
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for index, i in enumerate(countries):
    if i == "Finland":
        print(f"The country {i} has been found at index {index}")

# Zip example
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fruit": f, "veg": v})

print(fruits_and_veges)
