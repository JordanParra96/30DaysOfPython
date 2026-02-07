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
