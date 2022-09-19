print('********* SIMPLE IF and elif condtion blocks **********************\n\n')
x=int(input('**************Enter an inger value:**************\n'))
print('value of x is : ',x)
if x<10:
    print('{0} is less than 10'.format(x)) # if block
elif x>10 and x<30:
     print('{0} is between 11 and 29'.format(x))  # elif block
else:
    print('{0} is greater than 10'.format(x)) # else block
print('NESTED if conditions **********************\n\n')
x=int(input('Enter a integer number:\t'))

if x%2 == 0:
    print(x, ' is  factor of 2')
    if x%3 == 0:
        print(x, ' is  factor of 3')
        if x%5 == 0:
            print(x, ' is  factor of 5')
        else:
            print(x, ' is NOT factor of 5')

    else:
        print(x, ' is NOT factor of 3')
else:
    print(x, ' is NOT factor of 2')
    if x%3 ==0:
        print(x, ' is  factor of 3')
        if x%5 ==0:
            print(x, ' is  factor of 5')
        else:
            print(x, ' is NOT factor of 5')
    else:
        print(x, ' is NOT factor of 3')


print("+++++++++++++++++++++")
### Multi-way
print('is your number devidable by 2,3,5,15? ************\n\n')
x=int(input('Enter a integer number:\t'))
if x%2 ==0:
    print(x, ' is  factor of 2')
elif x%3 == 0:
    print(x, ' is  factor of 3')
elif x%5 ==0:
    print(x, ' is  factor of 5')

print('\n Using and or operator to combine expressions: \n')

age=int(input('Give us your age: \n'))
if age >= 18 and age <= 120:
    print("Welcome to the party ...")
    print("Let's have fun ...")
elif age<0:
    print('*** your value:  {} ********* you age must be positive value!!!!')
else:
    print("Sorry, you are not old enough to join to the Party!!!")
print("Done!")






