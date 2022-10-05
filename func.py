print('Understand Global variable and local variable in python functions\n')
var='this is a variable'

print(var)
var='change value'
def show_info():
    print(var)
def show_inf(var):
    print(var)
def show_info1(txt):
    txt.append(-1000)
    print(txt)    
show_info()    
show_inf('this is the text to be executed in show_info1 function')
show_inf(var)
print('\n\n we can pass a mutable object to the function like a list\n. it means we can modify list inside a funtion and use it outside of it.')
li=[i for i in range(200,1000, 100)]

show_info1(li)
print(li)
print('If we pass immutable variable like bool, int,string, float and change them inside a function then it will not effect variable outside a function.\n\n')
def show_info2(txt):
    txt=False
    print(txt)  

var2=True

show_info2(var2)
# print(var2)

print('Using function with just a empty ***return*** keyword. then the resutl is None ')
def show_info_with_return():
    
    print('inside funtion')
    return 

result=show_info_with_return()
print(result)
# you can return a value with a function
def show_info_with_return_1():
    
    print('inside funtion')
    return []
result=show_info_with_return_1()
print(type(result))
print(result)
# Functions can have more than 1 arguments 
def func_with_arguments(var1,var2,var3):
    print('this is the values passed to the function {0},{1},{2}'.format(var1,var2,var3))

func_with_arguments('name: Bill','family name: Smith ','age: 40')
# if we don't know how many arguments we want to pass to the function, 
# we use asteriks * attached to an argument like *args. 
print('If we use arbitary arguments in a function , then that args value is a tuple(immutable)')
def func_with_arguments(*args):
    print(type(args))
    print('this is the values passed to the function',args[:2])
    
def func_with_arguments_and_more(*args):
    print(type(args))
    print('this is the values passed to the function',args)

func_with_arguments(1,2,3,4,5)

dictionary={1:'name',2:'family'}
li=[1,2,3,4,5]
func_with_arguments_and_more(li)
func_with_arguments_and_more(dictionary)
# we can use positional arguments, it means we have key and value same as a dictionary .
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1="Emil", child3="Tobias", child2="Linus")
# a function can have arbitary *args and arbitary positional arguments(**kwargs)
def func_with_arguments_kwargs(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    print('this is the values passed to the function',args)
    print('this is the values passed to the function',kwargs)
    
func_with_arguments_kwargs([],{}) 

print('\nIf you add comments in the first line of a function then it will be useful to understand what your function does.')
def my_function(*args,**kwars):
  ''' this is the function that gets arbitary args and kwargs'''
#   """ The second way to add comments to the functions."""
  print('\nShow all the items in arbitary tuple',args)
  print("\nshow all the option in arbitray dictionary ", kwars)
my_function([1,2,3,4],child1="Emil", child3="Tobias", child2="Linus",child4='foo')