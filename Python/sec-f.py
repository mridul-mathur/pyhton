#tuple operations
tup1 = (1, 2, 3, 4, 5)
print('length of tuple: ', len(tup1))
print('First element of tuple: ', tup1[0])
print('Elements from 2nd to 4th: ', tup1[1:4])
y=list(tup1)
y.insert(2, 10)
tup1=tuple(y)
print('Updated tuple: ', tup1)
tup2 = (6, 7, 8, 9)
print('Concatenation of tuples: ', tup1 + tup2)
x=list(tup1)
x.pop(3)
tup1=tuple(x)
print('Removed 4rd element: ', tup1)
del tup2
try :
    print(tup2)
except Exception as e:
    print('tup2 is deleted')


# find the size of a tuple
tup1 = (1, 2, 3, 4)
print(len(tup1))


#find the maximum and minimum K elements in a tuple
tup1 = (100, 52, 33, 94, 51)


#create a list of tuples from given list having number and its cube in each tuple
list1 = [1, 2, 3, 4, 5]
print(list(map(lambda x: (x, x**3), list1)))