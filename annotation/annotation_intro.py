# def f(f):
#     f()
#     print('Hello decorator!!!')
#     return f

# def f2():
#     print('*******************************')

# x=f(f2)
# x()

def f3(func):
    def wrapper():
        print('started')
        func()
        print('Ended')
        
    return wrapper

@f3
def my_func():
    
    print('Hello')
my_func()
    