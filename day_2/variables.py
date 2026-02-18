''' Day 2: 30 Days of python programming '''

FIRST_NAME = 'Jordan'
LAST_NAME = 'Parra'
FULL_NAME = FIRST_NAME + ' ' + LAST_NAME
COUNTRY = 'Colombia'
CITY = 'Mosquera'
AGE = 29
YEAR = 2026
IS_MARRIED = False
IS_TRUE = True
IS_LIGHT_ON = True
one, two, three = 1, 2, 3

print('First Name type:', type(FIRST_NAME))
print('Last Name type:', type(LAST_NAME))
print('Full Name type:', type(FULL_NAME))
print('COUNTRY type:', type(COUNTRY))
print('CITY type:', type(CITY))
print('AGE type:', type(AGE))
print('YEAR type:', type(YEAR))
print('Is Married type:', type(IS_MARRIED))
print('Is True type:', type(IS_TRUE))
print('Is Light On type:', type(IS_LIGHT_ON))
print('One type:', type(one))
print('Two type:', type(two))
print('Three type:', type(three))

print('First name length:', len(FIRST_NAME))
print('Last name length:', len(LAST_NAME))

NUM_ONE = 5
NUM_TWO = 4
TOTAL = NUM_ONE + NUM_TWO
DIFF = NUM_ONE - NUM_TWO
PRODUCT = NUM_ONE * NUM_TWO
DIVISION = NUM_ONE / NUM_TWO
REMAINDER = NUM_ONE % NUM_TWO
EXP = NUM_ONE ** NUM_TWO
FLOOR_DIVISION = NUM_ONE // NUM_TWO

CIRCLE_RADIUS = 30
AREA_OF_CIRCLE = 3.14 * CIRCLE_RADIUS ** 2
CIRCUM_OF_CIRCLE = 2 * 3.14 * CIRCLE_RADIUS

input_radius = int(input('Enter radius: '))
AREA_OF_CIRCLE_input = 3.14 * input_radius ** 2
print('Area of circle with radius', input_radius, 'is:', AREA_OF_CIRCLE_input)

input_FIRST_NAME = input('Enter your first name: ')
input_LAST_NAME = input('Enter your last name: ')
input_COUNTRY = input('Enter your COUNTRY: ')
input_AGE = input('Enter your AGE: ')
