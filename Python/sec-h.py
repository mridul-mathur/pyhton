import math
# user defined function to swap two number and display number before swapping and after swapping.
n1 = int(input('Enter the 1st number: '))
n2 = int(input('Enter the 2nd number: '))
def swaps(n1, n2):
    print('Before swapping: (', n1, ',', n2, ')')
    n1, n2 = n2, n1
    print('After swapping: (', n1, ',', n2, ')')
swaps(n1, n2)


# calculate arithmetic operation on two number using user defined function
n1 = int(input('Enter the 1st number: '))
n2 = int(input('Enter the 2nd number: '))
def ops(n1, n2):
    print('Addition: ', n1+n2)
    print('Subtraction: ', n1-n2)
    print('Multiplication: ', n1*n2)
    print('Division: ', n1/n2)
ops(n1, n2)

# Calculate diameter and area of circle using user defined function
r = float(input('Enter the radius of circle: '))
def circle(r):
    d = float(2 * r)
    area = float(math.pi * (r**2))
    print('Diameter of circle: ', d, '\tArea of circle: ', area)


circle(r)


# function that takes three numbers as parameters, and returns the median value 
def median():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    c = int(input('Enter the third number: '))
    t1 = [a, b, c]
    t1.sort()
    print('The median is:', t1[1])


median()


# function that generates a random password


# Program to filter even values from list using lambda function
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('List: ', l1)
evel1 = list(filter(lambda x: x % 2 == 0, l1))
print('Even values from list: ', evel1)


# sum of elements of a list using lambda function
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda l: l[0] if len(l) == 1 else l[0] + f(l[1:])
sum = f(l1)
print('Sum of elements of list: ', sum)

# find small number between two numbers using Lambda function
n1 = int(input('Enter 1st number: '))
n2 = int(input('Enter 2nd number: '))
small = lambda n1, n2: n1 if n1 < n2 else n2
print('Smallest number: ', small(n1, n2))
