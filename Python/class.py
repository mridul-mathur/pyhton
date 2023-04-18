import math
# Grades = {'Sahil':90,'Abhijeet':65}
# print(Grades.keys())
# print(Grades.values())
# print(len(Grades))
# Grades['Kuruss']=99
# print(Grades)
# Grades['Abhijeet'] += 5
# print(Grades)
# del Grades['Abhijeet']
# print(Grades)
# print(Grades.items())
# dic1={}
# i=int(input("Enter the number of countries you want to enter: "))
# while(i>0):
#     country=input("Enter the country name: ")
#     captial=input("Enter the capital name: ")
#     dic1[country]=captial
#     i-=1
# print(dic1)

#convert milliseconds to hours, minutes and seconds
milli=int(input("Enter time in milliseconds "))
sec=(milli//1000)
minu=(sec//60)
hrs=(minu//60)
sec%=60;minu%=60;hrs%=24
print(hrs,":",minu,":",sec)