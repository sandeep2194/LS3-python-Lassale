
def positive(x):
    if x>0:
        return True
    else:
       return False
def positive1(x):
   return x>0

li=[1,0,-1,-3,2]
result=list(filter(positive1,li))
result1=list(filter(lambda x: x>0,li))
print(result)
print(result1)