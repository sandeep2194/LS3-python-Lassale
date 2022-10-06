
def get_max_of_items_v1(x:int, y:int, z:int)-> int:
    '''this function gets 3 values and return max one'''
    if x>y and x>z:
        return x
    elif y>z:
     return y
    else:
        return z
result=get_max_of_items_v1(10,22,30)
# print('the result is {0}'.format(result))
print(f'\nthe result is##################:\n\n\t\t max number is : {result}\n\n#########################')


# call a funtion inside another one 
def max_of_two_numbers(first_number,second_number):
    if first_number>second_number:
        return first_number
    return second_number


def get_max_of_items_v2(x:int, y:int, z:int)-> int:
    r1=max_of_two_numbers(y,z)
    r2=max_of_two_numbers(x,r1)
    return r2
   


def get_max_of_items_v3(x:int, y:int, z:int)-> int:
   return max_of_two_numbers(x,max_of_two_numbers(y,z))

result=get_max_of_items_v3(10,22,30)
# print('the result is {0}'.format(result))
print(f'\nthe result is##################:\n\n\t\t max number is : {result}\n\n#########################')



# factorial example(recursive programming)
'''
1- base stop condition and exit from your function
2- function calls itself 
'''
# what is a factorial of a number:  
# 5!= 5*4*3*2*1
def factorial(n):

    if n==0:
        return 1

    else:
       return n * factorial(n-1)


number=int(input('Enter a number to calculate a factorial of it : '))

result=factorial(number)
print(f'\nthe result of {number}! is ---> {result}\n')


