empty_list = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('length of numbers list:', len(numbers))
print('first element of numbers list:', numbers[0])
print('last element of numbers list:', numbers[-1])
print('element in the middle of numbers list:', numbers[len(numbers) // 2])
mixed_data_types = ['Jordan', 29, 172, 73, 'Married', 'Street 2345']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('it_companies list:', it_companies)
print('length of it_companies list:', len(it_companies))
print('first company:', it_companies[0])
print('last company:', it_companies[-1])
print('middle company:', it_companies[len(it_companies) // 2])
it_companies[0] = 'Meta'
print('it_companies after modification:', it_companies)
it_companies.append('Netflix')
it_companies.insert(len(it_companies) // 2, 'Salesforce')

it_companies[3] = it_companies[3].upper()
print('it_companies after additions and modification:', it_companies)
print('#, '.join(it_companies))
print('Is Google in it_companies list?', 'Google' in it_companies)
it_companies.sort()
print('Sorting it_companies list:', it_companies)
it_companies.reverse()
print('Reversing it_companies list in descending order:', it_companies)
first_three = it_companies[:3]
print('First three companies:', first_three)
last_three = it_companies[-3:]
print('Last three companies:', last_three)
middle_company = it_companies[len(it_companies) // 2:len(it_companies) // 2 + 1]
print('Middle company:', middle_company)
print('it_companies list before removal:', it_companies)
it_companies.pop(0)
print('it_companies list after removing last company:', it_companies)
it_companies.pop(len(it_companies) // 2)
print('it_companies list after removing middle company:', it_companies)
it_companies.pop()
print('it_companies list after removing last company:', it_companies)
print('it_companies list before clearing:', it_companies)
it_companies.clear()
print('it_companies list after clearing:', it_companies)
print('Deleting it_companies list...')
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print('Full stack development technologies:', full_stack)
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print('Full stack after adding Python and SQL:', full_stack)

# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('Sorted ages list:', ages)
min_age = ages[0]
max_age = ages[-1]
print('Minimum age:', min_age)
print('Maximum age:', max_age)
ages.append(min_age)
ages.append(max_age)
print('Ages list after adding min and max ages again:', ages)
median_age = (ages[len(ages) // 2] + ages[(len(ages) // 2) - 1]) / 2 if len(ages) % 2 == 0 else ages[len(ages) // 2]
print('Median age:', median_age)
average_age = sum(ages) / len(ages)
print('Average age:', average_age)
age_range = max_age - min_age
print('Age range:', age_range)
print('Comparing min and max age difference with average age:', abs(min_age - average_age), abs(max_age - average_age))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle_index = len(countries) // 2
print('Middle country/countries:', countries[middle_index])
first_half = countries[:middle_index]
second_half = countries[middle_index:]
print('First half of countries list:', first_half)
print('Second half of countries list:', second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print('China:', china)
print('Russia:', russia)
print('USA:', usa)
print('Scandic countries:', scandic_countries)