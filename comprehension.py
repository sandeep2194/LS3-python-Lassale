
list=[]
list.append(1)
list.append(2)

li=[]

for i in range(0,100):
    if i%2==0:
     li.append(i)

print(li)
x=False

if x:
    
 print ('the value is true')
else:
    print('value is false')

print('Use inline conding ')

print ('value is true') if x else print('value is false')

print('use list comprehension to add item to my list')
li_comprehension=[ i for i in range(0,100) if i%2!=0]
print(li_comprehension)


l1=[i for i in range(-100,-120,-1)]
l2=[i for i in range(0,1000,2)]

even_numbers=[i for i in l1 if i%2==0]
odd_numbers=[i for i in l2 if i%2!=0]

print(f'even values: ',even_numbers)
print(f'Odd values: ',odd_numbers)




