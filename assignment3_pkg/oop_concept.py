from random import randint

# question 5.1


class Student:

    student_count = 0

    def __init__(self, name, family_name, age, sin_number=''):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.__sin_number = sin_number
        Student.student_count += 1

    def get_sin_number(self):
        return self.__sin_number

    def set_sin_number(self):
        self.__sin_number = self.name[0] + \
            self.family_name[0]+str(randint(10000, 100000))

    def show_student_info(self):
        print("*******************************")
        print("Name: ", self.name)
        print("Family Name: ", self.family_name)
        print("Age: ", self.age)
        print("Sin Number: ", self.__sin_number)
        print("*******************************")

    @classmethod
    def number_of_students(self):
        return Student.student_count


# question 5.2
students = []
count = 0
while count < 4:
    name = input('Enter a name: ')
    family_name = input('Enter a family name: ')
    age = input('Enter age: ')
    stu = Student(name, family_name, age)
    stu.set_sin_number()
    students.append(stu)
    stu.show_student_info()
    count += 1

# question 5.3
print("Number of students created: ", Student.number_of_students())
