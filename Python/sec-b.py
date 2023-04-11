# Program for leap year
year = int(input("Enter the Year : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, " is a leap year.")
elif year % 100 == 0:
    print(year, " is not a leap year.")
else:
    print(year, " is not a leap year.")

# Largest in 3
a = int(input('enter first number : '))
b = int(input('enter second number : '))
c = int(input('enter third number : '))

if a > b and a > c:
    print(a, " : is the largest")
elif b > c:
    print(b, " : is the largest")
else:
    print(c, " : is the largest")


# Armstrong number or not
num = int(input("Enter the number : "))
temp = num
n = 0
while (temp != 0):
    temp //= 10
    n += 1
sum = 0
temp = num
while (temp != 0):
    rem = temp % 10
    sum = sum + (rem**n)
    temp //= 10
if sum == num:
    print(num, " is an Armstrong number")
else:
    print(num, " is not an Armstrong number")


# Roll number is even or not
roll = int(input('Insert your roll no. : '))
if roll % 2 == 0:
    print(roll, " : Roll number is even")
else:
    print(roll, " : Roll number is odd")


# Print grades of students
marks = int(input('Enter marks of student : '))
if marks >= 80:
    print("Student grade is Execellent")
elif marks >= 65 and marks < 80:
    print("Student grade is Good")
elif marks >= 50 and marks < 65:
    print("Student grade is Pass")
else:
    print("Student grade is Fail")
