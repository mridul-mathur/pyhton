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
