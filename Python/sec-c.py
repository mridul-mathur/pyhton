#print factorial of a number
def fact(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*fact(n-1)

n = int(input('Enter the num : '))
sol = fact(n)
print('The factorial is : ', sol)


#print prime numbe less then 20


#print multiplication table of any number
num = int(input('Enter the number : '))
n=1
for n in range(1,11):
    print(num ,'x' , n , ' = ', num*n)


#check for palindrome
num = int(input("Enter the number: "))
num = str(num)
rev_num = num[::-1]
if num == rev_num:
    print('The number is palindrome')
else:
    print('The number is not a palindrome')


# contruct the pattern: *
#                       **
#                       ***
#                       ****
#                       *****
#                       *****
#                       ****
#                       ***
#                       **
#                       *
def pypartup(n):
    if n==0:
        return
    else:
        pypartup(n-1)
        print("* "*n)
def pypartdown(n):
    for a in range( n+1, 0, -1):    
        for b in range(0, a - 1):  
            print("*", end=' ')  
        print(" ")

n = int(input("Enter number of max stars: "))
pypartup(n)
pypartdown(n)

#Fibonacci series
x = int(input('enter the number: '))
a , b = 0 , 1
if x<0:
    print('Enter a positive integer')
if x == 0:
    print(0)
elif x == 1:
    print(1)
else:
    for i in range(0, x):
        c = a + b
        a = b
        b = c
        print(b)