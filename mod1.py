'''
 python use module and packages to resolve namespaces problem. 
 Basically modules resolve collision of function and global varialbe names
 and
packages resolve colliton of module names in python file.(for example if you have 2 python files with the same name.)

 Every file in python  is a module if ends with .py
 Use import keyword to bring another file to your python file
 there are 2 ways to use import keyword
 1- use import key and the name of the module
    for example:
          import datatime
 2- use from keyword to bring specific members of a module to your python file
    for example:
        from datetime import datetime
you can use alias for a module or a member if you like by using as keyword
'''
from datetime import datetime as dt

def get_time():
 current_date_1=dt.now()
 print(f'GMT time is {current_date_1}')

def my_function():
    print ('hello world')



