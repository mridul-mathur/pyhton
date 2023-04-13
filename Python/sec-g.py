# demonstrate working with dictionaries
dict1 = {1: 'Mridul', 2: 'Sakshi', 3: 'Aashna', 4: 'Pawan'}
print(dict1)
dict1[5] = 'Lakshay'  # added to dict1
print(dict1)
dict1[5] = 'Lokii'  # edited dict1
print(dict1)
print(dict1[2])  # accessing element
del dict1[5]  # delete element
print(dict1)


# create a dictionary from a sequence
key = [100, 101, 102, 103]
data = ['Mridul', 'Sakshi', 'Aashna', 'Pawan']
dict1 = dict(zip(key, data))
print(dict1)


# Dictionary of numbers and their squares (i, i*i) from 1 to N
n = int(input('Enter the number of elements: '))
dict1 = dict()
for x in range(1, n+1):
    dict1[x] = x**2
print(dict1)
