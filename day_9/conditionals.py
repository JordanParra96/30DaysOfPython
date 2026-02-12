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