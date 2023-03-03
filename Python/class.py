s = "python programming"
print (s)
x = bool(s.islower())
y = bool(s.endswith('ing'))
print(y)
s1 ='hello'
s2 ='Hello'
s3 ='HELLO'

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sum = 0

for i in range(0, n + 1) :
    term = x**i
    print(term)
    sum += term

print("Sum =", sum)