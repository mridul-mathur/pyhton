#find factorial of a number using Recursion
def fact(n):
   if n == 1:
       return n
   else:
       return n * fact(n-1)
n=int(input("Enter a number: "))
print("Factorial :" , fact(n))

# fibonacci series using recursion
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter a number: "))
for i in range(0,n):
    print(fibo(i))
    
# find the sum of natural numbers using recursion
def sum():
    n = input("(blank to exit)Enter a number: ")
    if n == '':
        return 0
    else:
        n = int(n)
        return n + sum()
print("Sum: ",sum())