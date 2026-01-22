strings = ["Thirty", "Days", "Of", "Python"]
joined_string = " ".join(strings)
print(joined_string)

codingForAllStrings = ["Coding", "For", "All"]
joined_coding_string = " ".join(codingForAllStrings)
print(joined_coding_string)

company = "Coding For All"
print('Company:', company)
print('Length of company:', len(company))
print('Company in uppercase:', company.upper())
print('Company in lowercase:', company.lower())
print('Company capitalized:', company.capitalize())
print('Company title case:', company.title())
print('Company swapcase:', company.swapcase())
print('Slice first word:', company[0:6])
print('Does company contain "Coding"?', 'Coding' in company)
python4All = company.replace('Coding', 'Python')
print('Company after replacing "Coding" with "Python":', python4All)
python4Everyone = company.replace('Coding', 'Everyone')
print ('Company after replacing "All" with "Everyone":', python4Everyone)
print('Split company string using space as separator:', company.split(' '))
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('Companies:', companies.split(', '))
print('First character of company:', company[0])
print('Last character of company:', company[-1])
print('What chacter is at index 10?', company[10])
print('Acronym of company:', company[0] + company[5] + company[10])
print('Acronym of python4Everyone:', python4Everyone[0] + python4Everyone[5] + python4Everyone[10]  )
print('Index of first occurrence of "C" in company:', company.index('C'))
print('Index of first occurrence of "F" in company:', company.index('F'))
print('Index of last occurrence of "l" in company:', company.rindex('l'))
indexSentence = "You cannot end a sentence with because because because is a conjunction"
print('Index of first occurrence of "because" in sentence:', indexSentence.index('because'))
print('Index of last occurrence of "because" in sentence:', indexSentence.rindex('because'))
print('Slice "because" from the sentence:', indexSentence[31:54])
print('First occurrence of "because":', indexSentence.find('because'))
print('Does company start with "Coding"?', company.startswith('Coding'))
print('Does company end with "Coding"?', company.endswith('Coding'))
print('Remove whitespaces from both ends:', '   Coding For All   '.strip())
print('30DaysOfPython is isidentifier?:', '30DaysOfPython'.isidentifier())
print('thirty_days_of_python is isidentifier?:', 'thirty_days_of_python'.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('Join libraries with "# " as separator:', '# '.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(format('The area of a circle with radius {radius} is {area} square units.'))

a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')