
"""
price = 10
print(price)
# output will be 20 as python interpreter executes the code line by line



age = 20  # int
rating = 4.9  # float
nameis = 'mridul'  # string
is_new = True  # boolean

print(nameis, age, is_new)



# this will print the dictionary
def feat(a, b,n):
    c = a + b

    for i in range(0,n):
        i += c
        print(i)


feat(13.52, 20.34, 9)



name = input("What's your name: ")
print("Hey! " + name + " what's up?")


def change_name():
    print("enter your new name")
    new_name = input()
    name = new_name
    new_name = name
    print("your name has been changed to " + new_name)


def add_surname():
    print("enter your surname: ")
    surname = input()
    print("Full name: " + name + " " + surname)


print('how can i help you')
query = input()

if query == 'change my name':
    change_name()

if query == 'add surname':
    add_surname()
"""

set1 = {"Geeks", "For", "Geeks"}
print(set1)
