# Day 2: 30 Days of python programming
first_name = 'Jordan'
last_name = 'Parra'
full_name = first_name + ' ' + last_name
country = 'Colombia'
city = 'Mosquera'
age = 29
year = 2026
is_married = False
is_true = True
is_light_on = True
one, two, three = 1, 2, 3

print('First Name type:', type(first_name))
print('Last Name type:', type(last_name))
print('Full Name type:', type(full_name))
print('Country type:', type(country))
print('City type:', type(city))
print('Age type:', type(age))
print('Year type:', type(year))
print('Is Married type:', type(is_married))
print('Is True type:', type(is_true))
print('Is Light On type:', type(is_light_on))
print('One type:', type(one))
print('Two type:', type(two))
print('Three type:', type(three))

print('First name length:', len(first_name))
print('Last name length:', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

circle_radius = 30
area_of_circle = 3.14 * circle_radius ** 2
circum_of_circle = 2 * 3.14 * circle_radius

input_radius = int(input('Enter radius: '))
area_of_circle_input = 3.14 * input_radius ** 2
print('Area of circle with radius', input_radius, 'is:', area_of_circle_input)

input_first_name = input('Enter your first name: ')
input_last_name = input('Enter your last name: ')
input_country = input('Enter your country: ')
input_age = input('Enter your age: ')