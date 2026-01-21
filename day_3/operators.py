age = 29
height = 1.72
comp = 3 + 4j

# Area of a triangle
input_base = float(input('Enter base of the triangle: '))
input_height = float(input('Enter height of the triangle: '))
print('Area: ',0.5 * input_base * input_height)

# Perimeter of a triangle
input_side_a = float(input('Enter side a: '))
input_side_b = float(input('Enter side b: '))
input_side_c = float(input('Enter side c: '))
print('Perimeter: ', input_side_a + input_side_b + input_side_c)

# Area of a rectangle
input_length = float(input('Enter length of the rectangle: '))
input_width = float(input('Enter width of the rectangle: '))
print('Area: ', input_length * input_width)
# Perimeter of a rectangle
print('Perimeter: ', 2 * (input_length + input_width))

# Area of a circle
input_radius = float(input('Enter radius of the circle: '))
pi = 3.14
print('Area: ', pi * input_radius ** 2)
# Circumference of a circle
print('Circumference: ', 2 * pi * input_radius)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2
# Slope
slope_line = m
# x-intercept (set y=0)
x_intercept = -b / m
# y-intercept (set x=0)
y_intercept = b
# Slope between point (2, 2) and (6, 10)
point_a = (2, 2)
point_b = (6, 10)
slope = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
print('Slope of the line:', slope_line)
print('x-intercept:', x_intercept)
print('y-intercept:', y_intercept)
print('Slope between points (2,2) and (6,10):', slope)
# Compare the slopes
print('Are the slopes equal?', slope_line == slope)
# Euclidean distance between (2, 2) and (6, 10)
euclidean_distance = ((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5
print('Euclidean distance between (2,2) and (6,10):', euclidean_distance)

# comparison operators
python_len = print(len('python'))
dragon_len = print(len('dragon'))
print('Are the lengths equal?', python_len == dragon_len)
print('Is "on" in "python"?', 'on' in 'python')
print('Is "on" in "dragon"?', 'on' in 'dragon')
print('Is "jargon" in "I hope this course is not full of jargon"?', 'jargon' in 'I hope this course is not full of jargon')
print('Is "on" not in "dragon"?', 'on' not in 'dragon')
print('Is "on" not in "python"?', 'on' not in 'python')
print('str(float(len("python"))):', str(float(len('python'))))

# Even numbers  
number = int(input('Enter a number: '))
is_even = number % 2 == 0
print('Is the number even?', is_even)

print('floor division of 7 // 3 is equal to int 2.7:', 7 // 3 == int(2.7))
print('type of "10" is equal to type of 10:', type('10') == type(10))
print('int("9.8") is equal to 10:', int(float('9.8')) == 10)

# Calculate weekly earning
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print('Your weekly earning is:', hours * rate_per_hour)

# Calculate the number of seconds a person has lived
num_of_years = int(input('Enter number of years you have lived: '))
print('You have lived for', num_of_years * 365 * 24 * 60 * 60, 'seconds.')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')