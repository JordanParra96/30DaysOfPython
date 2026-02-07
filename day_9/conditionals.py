age = int(input('Enter your age: '))
if age < 18:
    years_needed = 18 - age
    print(f'You need {years_needed} more years to learn to drive.')
else:
    print('You are old enough to learn to drive.')