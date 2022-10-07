# in order to iterate through a dictionary 
# we can use for loop and have key and value both for each item
# Each dictionary has a function named items() which is a iterable funtion.

dictionary=dict()

dictionary={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'Jul',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
#key and value are variables,So you can change them for example to k,v 
for (key,value) in dictionary.items():
    print (f'\tkey is {key} and value is {value}\n')


# It is possible to use comprehension with for loop too.

even_months=[ v for (k,v) in dictionary.items() if k%2==0]
odd_months=[ v for (k,v) in dictionary.items() if k%2!=0]
print(f'Even Months: {even_months}\n\n')
print(f'Odd Months: {even_months}\n\n')