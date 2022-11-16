class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
class Teacher(Person):
  __rate=1.04
  def __init__(self,fname,lname,courses,experience=1):
    # call __init__ from super class
    super().__init__(fname,lname)
    self.courses=courses
    self.experience=experience
    self.teacher_rate=Teacher.__rate
  # how to calculate salary   salary=rate*experience*base_salary
  def calculate_salary(self,base_salary:float)->float:
    '''
        document for a method (doc)
        this mehtod calculates the salary based on experience and rate 
    '''
    salary=self.teacher_rate*self.experience*base_salary
    return salary
  def promote(self,percentage):
    self.teacher_rate=(1+percentage)*self.teacher_rate


p = Person("John", "Doe")
p.printname() 
teacher_list=['420-SL3-AS','420-EL2-AS','420-JV4-AS']
leo=Teacher('Leo','Page',teacher_list,5)
# leo.printname()
# print(leo.courses)
stepto=Teacher('Bill','Stepto',['420-SL3-AS'])
leo.promote(.25)
print(leo.calculate_salary(20000))
stepto.promote(.2)
print(stepto.calculate_salary(20000))


def start_game(level:int,name:str,players:int,online:bool)-> None:
      '''
        document for a start_gamme (doc)
        this mehtod will start the game easily 
      '''
      print(f'game has been started\nlevel={level}\nname:{name}')
      print(f'\nplayers:{players}\nonline:{online}')    






start_game()





