def parent():
    print('Printing form the parent() funciton.')
    
    # add 2 function with definitions
    def first_child():
            print('Printing form the first_child() funciton.')
    def second_child():
            print('Printing form the second_child() funciton.')
    
    second_child()
    first_child()
    
parent()     

def f(f):
    f()
    print('Hello decorator!!!')
    return f

def f2():
    print('*******************************')

x=f(f2)
x()

def f3(func):
    def wrapper():
        print('started')
        func()
        print('Ended')
        
    return wrapper

def hello():
    print('Hello')
h=f3(hello)
h()
w=f3(lambda: print('Hello'))
w()

def f3(func):
    x=5
    y=7
    def wrapper():
        print('started')
        print('called from outside of wrapper:{0} '.format(func(x,y)))
        print('Ended')
        
    return wrapper
def sub(a,b):
    return a-b
result =f3(lambda a,b:a-b)
result1 =f3(sub)
print('\n******call Wrapper funtion with lambda   f3(lambda a,b:a-b)')
result()
print('\n******call funtion with function name f3(sub) ')
result1()
