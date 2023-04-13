# Operations of list
list1 = [12, 23, 34, 45]
print("First element: ", list1[0])
print("Repetition 2 times: ", list1*2)  # repetition
print('Length of the list: ', len(list1))  # length
list1 = list1[::-1]  # elements in reverse order
print('Reverse order: ', list1)
list1.pop(2)  # remove 3rd element
print('removed 3rd element: ', list1)
list1.insert(1, 100)
print('inserted element at 2nd index: ', list1)  # insert 3rd element
print('Sorted list: ', sorted(list1))  # sorted list
list2 = [89, 56, 67, 78, 90]
print('Concatenation of lists: ', list1 + list2)  # concatenation
print("1st to 3rd elements: ", list1[0:3])  # slicing
print("element '45' in list?", 45 in list1)  # membership


# even numbers in a list
list1 = [12, 23, 34, 45, 56, 67, 78, 89, 90]
for i in list1:
    if i % 2 == 0:
        print(i, end=" ")
print()


# interchange first and last element of a list
list1 = [1, 2, 3, 4, 5]
(list1[0], list1[-1]) = (list1[-1], list1[0])
print(list1)


# turn every item of a list into its square
list1 = [1, 2, 3, 4, 5]
print('Squared each element of the list: ',  [i**2 for i in list1])


# replace list’s item with new value
list1 = ['Mrid', 'Sakshi', 'Mrid', 'Pawan', 'Aashna', 'Mrid']
for i in range(len(list1)):
    if list1[i] == 'Mrid':
        list1[i] = 'Mridul'
print(list1)


# find the position of minimum and maximum elements of a list
list1 = [86, 31, 92, 21, 1, 43, 74, 56]
print('Minimum element at index: ', list1.index(min(list1)))
print('Maximum element at index: ', list1.index(max(list1)))


# cumulative sum of elements of a list
list1 = [1, 2, 3, 4, 5]
for i in range(1, list1[-1]):
    list1[i] += list1[i-1]
print(list1)


#Write a program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line.
list1 = []
val = int(input('Enter a number (0 to exit): '))
while val != 0:
    val = int(input('Enter a number (0 to exit): '))
    if val != 0:
        list1.append(val)
    else:
        list1.sort()
        print('Sorted list: ', list1)
        for i in list1:
            print(i)


#Write a program that reads integers from the user until a blank line is entered. Once all of the integers have been read your program should display all of the negative numbers, followed by all of the zee, followed by all of the positive numbers. Within each group the numbers should be displayed in the same order that they were entered by the user.
pos = []
zee = []
neg = []
num = input('Enter a number (blank to exit): ')
while num != '':
    val = int(num)
    if val > 0:
        pos.append(val)
    elif val < 0:
        neg.append(val)
    else:
        zee.append(val)
    num = input('Enter a number (blank to exit): ')
for i in neg, zee, pos:
    for j in i:
        print(j, end=", ")


# check all elements are unique or not in Python
