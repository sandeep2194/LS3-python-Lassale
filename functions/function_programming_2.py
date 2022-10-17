
# from functools import reduce
# predicate which is a true or fale in the return value.  
def negative(x):
    return x<0

# print(negative(-10))
print('list of items from -5 to 15 saved in the list.\n')
li =[i for i in range(-5,15,1) ]
print(li)

negative_filter=filter(negative,li)
result_of_filter=list(negative_filter)
print('result of a filter using nagative function and our li list \n')
print(result_of_filter)

#print("##############  to use lambda and clean coding of previous example: #####")
print(list(filter(lambda x: x < 0, li)))

print("############## python way if we don't want a list #####")
print(list(filter(lambda x: x < 0, [i for i in range(-5,15,1) ])))
'''
traditional way of using map
li=[1,2,3,4,5]
res=[]
for x in li:
    double_value=addition(x)
    res.append(double_value)
print(res)
'''
print("Using map in python")

def addition(n):
    # res=n+n
    return n+n
print(addition(100))

li=[1,2,3,4,5]
result=list(map(addition,li))
print(result)
print(f'\n\npythonic and concise way --> {list(map(addition,li))}\n')

even_numbers=[ i  for i in range(-100,100,1) if i%2==0]
print(f'Before Using map:\n{even_numbers}')
res=list(map(addition,even_numbers))
print(f'After using map:\n{res}')
round(10.88383954958498549584958,2)
float_numbers=[i*0.3343 for i in range(1,1000,1)]
#case 1: create a mapping funtions that get float_numbers and map them with 2 decimal places.
def round_me(x):
    return round(x,2)

print('using funtion round_me and float_numbers list and map the data\n')
print(list(map(round_me,float_numbers)))
print('Pythonic of previous example:\n')
result_2_decimal=list(map(lambda x: round(x, 2), [i*.3343 for i in range(1,1000,1)]))


# for x in list(map(lambda x: round(x, 2), float_numbers)):
#     print(x)

filter_grather_than_40= list(filter(lambda x:x>40,result_2_decimal))

for y in filter_grather_than_40:
    print(y)

print("Using reduce from functools module in python.\n")
print("We can use from and import keyword every where in our python file.")
print("but it is better to use them on the top of your file. then it is easy to add or remove more ")

from functools import reduce

def add_two_numbers(a,b):
    result=a+b
    print(f'{a} + {b} = {result}')
    return result

# print(add_two_numbers(4,9))

nums=[0,1,2,3,4,5]
res=0
for x in nums:
    res=res+x

print(f'using traditional way with a fucntion and loop --> {res}\n')
print(nums)

comment='''
Reduce function needs 2 paramters.
1- a function with 2 arguments same as add_two_numbers
2- an itrable object which is nums here
reduce(add_two_numbers,nums)
Don't forget --> The result of reduce in python is a cummulitive value.

'''
print (comment)


result_of_reduce=reduce(add_two_numbers,nums)
print(f'Result of using reduce fucntion -->  {result_of_reduce}')

print(f'Using lambda in reduce {reduce(lambda x,y:x+y,nums)}')







