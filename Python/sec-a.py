import random
import math


# data types in python
a = 20  # int
b = 4.9  # float
c = 3 + 5j  # complex
nameis = 'mridul'  # string
is_new = True  # boolean

print(type(a))
print(type(b))
print(type(c))
print(type(nameis))
print(type(is_new))


# Arithmetic operators
x = 15
y = 10

print("sum is ", x+y)
print("substraction is ", x-y)
print("product is ", x*y)
print("float division is ", x/y)
print("int division is ", x//y)
print("modulus is ", x % y)
print("exponent is ", x**y)


# Random numbers
print(random.randint(1, 6))


# Swapping Program
print(x, y)
x = x ^ y
y = x ^ y
x = x ^ y

print("Swapped: ", x, y)


# Volume of a sphere
r = float(input("Enter radius of sphere : "))
v = 4*(math.pi)*(r**3)/3

print("Volume of sphere is : ", v)