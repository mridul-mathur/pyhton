import math
# Write a Program to write user defined function to swap two number and display number before swapping and after swapping.
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
print('Before swapping: (', n1, ',', n2, ')')
n1, n2 = n2, n1
print('After swapping: (', n1, ',', n2, ')')


#calculate arithmetic operation on two number using user defined function


#Calculate diameter and area of circle using user defined function
r = float(input('Enter the radius of circle: '))
def circle(r):
    d = float(2 * r)
    area = float(math.pi * r * r)
    return d, area
d, area = circle(r)
print('Diameter of circle: ', d, '\tArea of circle: ', area)


#function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=int(input('Enter the third number: '))
def median(a,b,c):
    t1=[a,b,c]
    t1.sort()
    return t1[1]
print ('The median is:', median(a,b,c))