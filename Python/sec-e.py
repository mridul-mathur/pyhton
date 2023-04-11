# Operations of list
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(list1*2)  # repetition
print(list1 + list2)  # concatenation
print(len(list1))  # length
for i in list1:  # iteration
    print(i)
print(34 in list1)  # membership


# even numbers in a list
for i in list1:
    if i % 2 == 0:
        print(i)


# interchange first and last element of a list
(list1[0], list1[-1]) = (list1[-1], list1[0])
print(list1)


#turn every item of a list into its square
list2=[]
for i in list1:
    list2.append(i**2)
    print(list2)


#check all elements are unique or not in Python


#replace list’s item with new value


#find the position of minimum and maximum elements of a list


#cumulative sum of elements of a list
for i in range(1,list1[-0]):
    list1[i] += list1[i-1]
print (list1)