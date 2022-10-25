
class Employee:
  '''
  This is the class definitoin 
  '''
  emp_count=0
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    Employee.emp_count+=1
  def show_inf(self):
    print(f'employee name={self.name} and salary is {self.salary} $')
emp1=Employee('Bill',120000)
emp2=Employee('Jane',120001)

print(Employee.emp_count)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("\n\n\Employee.__dict__:\n\n", Employee.__dict__)

