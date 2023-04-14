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


#Write a Program that determines and displays the number of unique characters in a string entered by the user. For example, “Hello, World!” has 10 unique characters while “zzz”
str1 = input('Enter the string: ')
unique = {}
for x in str1:
    if x not in unique:
        unique[x]= 1
print('Number of unique characters: ', len(unique))


#wo words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one ‘e’, one ‘I’, one ‘l’, and one ‘v’. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.
str1=input('Enter the first string: ')
str2=input('Enter the second string: ')
count={}
def counting(s):
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count
count1 = counting(str1)
count2 = counting(str2)
if   count1 == count2:
      print ("Those strings are anagrams.")
else :
      print ("Those strings are not anagrams.")
