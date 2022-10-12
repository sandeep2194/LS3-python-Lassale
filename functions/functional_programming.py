
# predicate means, there is a true or false from a function or lambda 
def positive(x):
    if x>0:
        return True
    else:
       return False
def positive1(x):
   return x>0

li=[1,0,-1,-3,2]
print('\n******filter built-in function is an itrable object , we change it to list ')
print('\n******filter(function, itarable)')
result=list(filter(positive1,li))
print(f'Using of a function in filter as a predicate function named positive1:\n{result}')
result_using_lambda=list(filter(lambda x: x>0,li))
print(f'Using of a lambda in filter as a predicate function, there is no name for lambda:\n{result_using_lambda}')