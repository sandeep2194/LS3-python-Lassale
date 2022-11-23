print('Handle Exceptions')
try:
    print(x)
except:
    print('value has not been defined!!!')
    

print('Raise an exception')
x=-1
try:
    if x<0:
        raise Exception(' ******value is not less than 0')
except Exception as e:
   print(e)

import sys
import os

def check():
    try:
        while True:
            x=int(input('To exist type 0: '))
            if x==0:
                sys.exit()
    except ValueError as e:
        print('Value exception occured !!!')
        print(e)
        check()
    except SystemExit:
          print('System exit has been called')
    finally:
        print('Bye Bye !!!!!')
check()
number=10
from sl3_exception.my_exceptions import ValueTooLarge,ValueTooSmallError
while True:
    try:
        i_num=int(input('Guess a number between 1 to 20 ? :'))
        if i_num<number:
            raise ValueTooSmallError('This value is too small, try again!!')
        elif i_num>number:
            raise ValueTooLarge('This value is to large , try agian!!')
        break
    except ValueTooSmallError as e:
        print(e.args)

    except ValueTooLarge as e:
        print(e)

print('Congrad you guess the right number')
