name = input("What's your name: ")
print("Hey! " + name + " what's up?")

def change_name():
    print("enter your new name")
    new_name = input()
    temp = new_name



    print("your name has been changed to " + name)

def add_surname():
    print("enter your surname: ")
    surname = input()
    print("Full name: " + name + " " + surname)

query = 'Yes'
while query!='no':
    print('how can i help you')
    query = input()

    if query == 'change my name':
        change_name()

    if query == 'add surname':
        add_surname()