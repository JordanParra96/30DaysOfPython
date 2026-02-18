''' Day 10: 30 Days of python programming '''

# Level 1
from countries_data import countries_data
from countries import countries

count_var = 0
while count_var < 11:
    print('while count:', count_var)
    count_var += 1

for i in range(11):
    print('for count:', i)

for i in range(10, -1, -1):
    print('for reverse:', i)

count_reverse = 10
while count_reverse > -1:
    print('While reverse:', count_reverse)
    count_reverse -= 1

triangle_var = '#'
for i in range(7):
    print(triangle_var)
    triangle_var += '#'

for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

for i in range(11):
    print(f'{i} x {i} = {i * i}')

languages_lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lan in languages_lst:
    print(lan)

for i in range(101):
    if i % 2 == 0:
        print(f'Even: {i}')
    elif i % 2 != 0:
        print(f'Odd: {i}')

# Level 2
SUM = 0
for i in range(101):
    SUM += i
print(f'Sum of numbers from 0 to 100 is: {SUM}')

SUMEVEN = 0
SUMODD = 0
for i in range(101):
    if i % 2 == 0:
        SUMEVEN += i
    elif i % 2 != 0:
        SUMODD += i
print(f'Sum of even numbers from 0 to 100 is: {SUMEVEN}')
print(f'Sum of odd numbers from 0 to 100 is: {SUMODD}')

# Level 3

for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
REVERSED_FRUIT = []
for fruit in range(len(fruits)):
    REVERSED_FRUIT.append(fruits[len(fruits) - 1 - fruit])
print(REVERSED_FRUIT)

languages = set()
for country in countries_data:
    for language in country['languages']:
        languages.add(language)
print(f'Total number of languages: {len(languages)}')

language_count = {}
for country in countries_data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
sorted_languages = sorted(language_count.items(),
                          key=lambda x: x[1], reverse=True)
print('Ten most spoken languages:')
for i, (language, count) in enumerate(sorted_languages[:10]):
    print(f'{i+1}. {language}: {count}')

sorted_countries = sorted(
    countries_data, key=lambda x: x['population'], reverse=True)
print('Ten most populated countries:')
for i, country in enumerate(sorted_countries[:10]):
    print(f'{i+1}. {country["name"]}: {country["population"]}')
