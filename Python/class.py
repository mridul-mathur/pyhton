from math import gcd
import random
lis = []
for i in range(10):
    lis.append(random.randint(0, 100))
print(lis)
even = []
odd = []
for i in lis:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers are: ", even)
print("Odd numbers are: ", odd)

lis1 = [99, 21, 72, 66, 54, 63]
gcd = gcd(lis1[0], lis1[1])
print(gcd)
i = 2
while i < len(lis1):
    gcd = gcd(gcd, lis1[i])
    i += 1
print("GCD is: ", gcd)
