next=int(input('*****************\ngive a number: '))
 
while(next<100):
    print('I know how a while loop works')
    next+=1
 
print('I am out of the loop')
 
x=1
while(x<=100):
    if x>50:
         print('+++++++ {0}\t+++++++'.format(x))
    else:
        print('****** {0}\t*********'.format(x))
    x+=1
 
print('\nI am out of the loop')
 
print('\n Change increment to have different resutls ')
while(x<=100):
  print('+++++++ {0}\t+++++++'.format(x))
  x+=5


print('while loop with break statement.')
x=0
while True:
    print(x)
    x+=1
    break