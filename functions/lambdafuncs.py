


def lm(x):
    return x

y=lambda x:x
print(y(3))

print((lambda x:x)(4))

def add(x):
    return x+5
def addition(x,y):
    return x+y

f=lambda x: x+5
result =(lambda x: x+5)(6)
print(f'from lambda : {f(5)}')
print(f'from ordinary function:  {add(5)}')
print(f'2nd version of lambda function:  {result}')
print(f'3nd version of lambda function:  {(lambda x: x+5)(6)}')
print(f'lambda with 2 arguments :  {(lambda x,y: x+y)(6,7)}')



