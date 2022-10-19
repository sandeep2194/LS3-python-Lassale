# 
# d=Dict()
class Dog:
    def __init__(self,name,breed,age):
       self.name=name
       self.breed=breed
       self.age=age
    
    #behaviour 
    def make_noise(self):
        print(f'woof woof from {self.name}')
    def walk(self):
        print(f'I am walking from {self.name}')
    def smell(self):
        print(f'I am searching from {self.name}')
        
nick=Dog('Nick','Hoskey',3)
dummy=Dog('dummy','Podle',10)
tommy=Dog('tommy','Shiba Inu',7)
nick.make_noise()
dummy.smell()
tommy.walk()

# class Student:
#    def __init__(self,name,age,country):
#        self.name=name
#        self.age=age
#        self.country=country
#        pass

# student1=Student('Jane',23,'CANADA')
# print(student1.name)
# print(student1.age)
# print(student1.age)
# student_list=list()
# for i in range(0,3):
#    name= input('give your name: ')
#    age= int(input('enter your age:'))
#    country= input('Enter your country: \t')
#    student=Student(name,age,country)
#    student_list.append(student)