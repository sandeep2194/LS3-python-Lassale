class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Teacher(person):
    pass


p = person("john", "doe")
p.printname()


teacher = Teacher('leo', 'page')
teacher.printname()
