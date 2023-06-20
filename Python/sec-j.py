# constructor and destructor
class Animals:
    def __init__(self):
        print('The class called Animals is CREATED.')
    def __del__(self):
        print('The destructor is called for deleting the Animals.')
object = Animals()
del object

# getter and setter
class Stud:
    def __init__(self):
        self.__name = 'Mridul'
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
object = Stud()
print(object.get_name())
object.set_name('Sakshi')
print(object.get_name())

# calc grade of student

class Student:
    def __init__(self , n ='' , p =0):
        self.name = n
        self.per = p
    def calcgrade(self):
        if self.per > 80:
            return 'A'
        elif self.per > 60 & self.per <= 80:
            return 'B'
        elif self.per > 40 & self.per <= 60:
            return 'C'
        else:
            return 'F'
st = Student('Mridul' , 90)
print(st.calcgrade())
st = Student('Sakshi' , 80)
print(st.calcgrade())

# single inheritance
class Std_Name:
    def __init__(self , n = ''):
        self.name = n
class Std_Roll(Std_Name):
    def __init__(self , n = '' , r = 0):
        Std_Name.__init__(self , n)
        self.roll = r
    def display(self):
        print('Name: ' , self.name)
        print('Roll: ' , self.roll)
st_r = Std_Roll('Mridul' , 425)
st_r.display()


# multilevel inheritance
class St_Name:
    def __init__(self , n = ''):
        self.name = n
class St_Roll(Std_Name):
    def __init__(self , n = '' , r = 0):
        St_Name.__init__(self , n)
        self.roll = r
class St_Marks(Std_Roll):
    def __init__(self , n = '' , r = 0 , m = 0):
        St_Roll.__init__(self , n , r)
        self.marks = m
    def display(self):
        print('Name: ' , self.name)
        print('Roll: ' , self.roll)
        print('Marks: ' , self.marks)
st_m = St_Marks('Mridul' , 425 , 90)
st_m.display()