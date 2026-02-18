''' Day 4: 30 Days of python programming '''

STRINGS = ["Thirty", "Days", "Of", "Python"]
JOINED_STRING = " ".join(STRINGS)
print(JOINED_STRING)

codingForAllStrings = ["Coding", "For", "All"]
JOINED_COSING_STRING = " ".join(codingForAllStrings)
print(JOINED_COSING_STRING)

COMPANY = "Coding For All"
print('Company:', COMPANY)
print('Length of company:', len(COMPANY))
print('Company in uppercase:', COMPANY.upper())
print('Company in lowercase:', COMPANY.lower())
print('Company capitalized:', COMPANY.capitalize())
print('Company title case:', COMPANY.title())
print('Company swapcase:', COMPANY.swapcase())
print('Slice first word:', COMPANY[0:6])
print('Does company contain "Coding"?', 'Coding' in COMPANY)
PYTHON4ALL = COMPANY.replace('Coding', 'Python')
print('Company after replacing "Coding" with "Python":', PYTHON4ALL)
PYTHON4EVERYONE = COMPANY.replace('Coding', 'Everyone')
print('Company after replacing "All" with "Everyone":', PYTHON4EVERYONE)
print('Split company string using space as separator:', COMPANY.split(' '))
COMPANIES = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('Companies:', COMPANIES.split(', '))
print('First character of company:', COMPANY[0])
print('Last character of company:', COMPANY[-1])
print('What chacter is at index 10?', COMPANY[10])
print('Acronym of company:', COMPANY[0] + COMPANY[5] + COMPANY[10])
print('Acronym of python4Everyone:',
      PYTHON4EVERYONE[0] + PYTHON4EVERYONE[5] + PYTHON4EVERYONE[10])
print('Index of first occurrence of "C" in company:', COMPANY.index('C'))
print('Index of first occurrence of "F" in company:', COMPANY.index('F'))
print('Index of last occurrence of "l" in company:', COMPANY.rindex('l'))
INDEXSENTENCE = "You cannot end a sentence with because because because is a conjunction"
print('Index of first occurrence of "because" in sentence:',
      INDEXSENTENCE.index('because'))
print('Index of last occurrence of "because" in sentence:',
      INDEXSENTENCE.rindex('because'))
print('Slice "because" from the sentence:', INDEXSENTENCE[31:54])
print('First occurrence of "because":', INDEXSENTENCE.find('because'))
print('Does company start with "Coding"?', COMPANY.startswith('Coding'))
print('Does company end with "Coding"?', COMPANY.endswith('Coding'))
print('Remove whitespaces from both ends:', '   Coding For All   '.strip())
print('30DaysOfPython is isidentifier?:', '30DaysOfPython'.isidentifier())
print('thirty_days_of_python is isidentifier?:',
      'thirty_days_of_python'.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('Join libraries with "# " as separator:', '# '.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

RADIUS = 10
AREA = 3.14 * RADIUS ** 2
print(
    format('The area of a circle with radius {RADIUS} is {AREA} square units.'))

A = 8
B = 6
print(f'{A} + {B} = {A + B}')
print(f'{A} - {B} = {A - B}')
print(f'{A} * {B} = {A * B}')
print(f'{A} / {B} = {A / B}')
print(f'{A} % {B} = {A % B}')
print(f'{A} // {B} = {A // B}')
print(f'{A} ** {B} = {A ** B}')
