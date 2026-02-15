# Level 1
count = 0
while count < 11:
    print('while count:', count)
    count += 1

for i in range(11):
    print('for count:', i)

for i in range(10, -1, -1):
    print('for reverse:', i)

countReverse = 10
while countReverse > -1:
    print('While reverse:', countReverse)
    countReverse -= 1

triangle = '#'
for i in range(7):
    print(triangle)
    triangle += '#'

for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

for i in range(11):
    print(f'{i} x {i} = {i * i}')

languages_lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lan in languages_lst:
    print(lan)

for i in range(101):
    if i % 2 == 0:
        print(f'Even: {i}')
    elif i % 2 != 0:
        print(f'Odd: {i}')

# Level 2
sum = 0
for i in range(101):
    sum += i
print(f'Sum of numbers from 0 to 100 is: {sum}')