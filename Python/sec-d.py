# create, concatenate, string, accessing sub-string from a given string.
s1 = input("Enter first String : ")
s2 = input("Enter second String : ")
print("First string is : ", s1)
print("Second string is : ", s2)
print("concatenations of two strings :", s1+s2)
print("Substring of given string :", s1[1:4])


# length of a string
name = 'Mridul'
print('Length of String: ', len(name))


# check for palindrome in strings
name = input('enter the string: ')
rev_name = name[::-1]
if name == rev_name:
    print('The string is palindrome')
else:
    print('The string is not a palindrome')


# count all letters, digits, and special symbols from a given string
str1 = input('Enter the string: ')
alpha, num, symb = (0, 0, 0)
for i in str1:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        num += 1
    else:
        symb += 1
print('Number: ', num, ' Alphabets: ', alpha, ' Symbols: ', symb)


# sum and average of the digits present in your registration number
Reg_no = int(input('Enter your registration number: '))
sum = 0
n = 0
while (Reg_no > 0):
    digit = Reg_no % 10
    sum += digit
    Reg_no //= 10
    n += 1
avg = sum/n
print('Sum: ', sum, ' Average: ', avg)
