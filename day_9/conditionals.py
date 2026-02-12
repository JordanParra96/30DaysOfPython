your_age = int(input('Enter your age: '))
if your_age < 18:
    years_needed = 18 - your_age
    print(f'You need {years_needed} more years to learn to drive.')
else:
    print('You are old enough to learn to drive.')

my_age = 29
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print(f'I am {age_diff} year older than you.')
    else:
        print(f'I am {age_diff} years older than you.')
elif my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print(f'You are {age_diff} year older than me.')
    else:
        print(f'You are {age_diff} years older than me.')

number_one = int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))

if number_one > number_two:
    print(f'{number_one} is greater than {number_two}.')
elif number_one < number_two:
    print(f'{number_one} is less than {number_two}.')
else:
    print(f'{number_one} is equal to {number_two}.')

# Level 2
grade = int(input('Enter your grade: '))

if grade >= 90 and grade <= 100:
    print('Your grade is A.')
elif grade >= 80 and grade < 90:
    print('Your grade is B.')
elif grade >= 70 and grade < 80:
    print('Your grade is C.')
elif grade >= 60 and grade < 70:
    print('Your grade is D.')
elif grade >= 0 and grade < 60:
    print('Your grade is F.')

month = input('Enter the month: ').title()
if month in ['September', 'October', 'November']:
    print('The season is Autumn.')
elif month in ['December', 'January', 'February']:
    print('The season is Winter.')
elif month in ['March', 'April', 'May']:
    print('The season is Spring.')
elif month in ['June', 'July', 'August']:
    print('The season is Summer.')

fruits = ['banana', 'orange', 'mango', 'lemon']
input_fruit = input('Enter a fruit: ').lower()
if input_fruit in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(input_fruit)
    print(fruits)

# Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print('Middle skill:', person['skills'][len(person['skills']) // 2])
    if 'Python' in person['skills']:
        print('Python is one of the skills.')
    else:
        print('Python is not one of the skills.')
    if person['skills'] == ['JavaScript', 'React']:
        print('He is a front end developer.')
    elif person['skills'] == ['Node', 'Python', 'MongoDB']:
        print('He is a backend developer.')
    elif person['skills'] == ['React', 'Node', 'MongoDB']:
        print('He is a fullstack developer.')
    else:
        print('unknown title.')

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

