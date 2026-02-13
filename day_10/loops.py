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