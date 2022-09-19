# ******************** tuple********************


ll=['Jan','Feb','March']
tt=('Jan','Feb','March')

print('The type of this data structure is : ',type(tt))
print('The type of this data structure is : ',type(ll))

Tuple=('d',12,'string',True)
# print(Tuple[11]) # this is an error since item 11 doesn't exist in Tuple 
print(Tuple[:])

t1=(100,200,300,400,500)
print('create new tuple with the other tuple')
t8_new =(50,)+t1[0:]
print(t8_new)
t8_new =t1[:]+(50,)
print(t8_new)

print(t8_new[:3]+(800,))
print('\n\n\n')
print(t8_new)

list_of_classes=('Math','Physic','Chemistry','English')
print('**************** multi dimentional tuple ****************** \n')
nested_tuple=(('Math','Physics','Chemistry','English'),('Math2','French'))

print('print all items in  Tuple')
print(nested_tuple)
print('\nall item from first tuple in outer tuple')
print(nested_tuple[0][:])
print('\nget items of first inner tuple from 0 to 2')
print(nested_tuple[0][2])

print('\nusing operator for tuple:\n')
print(list_of_classes*2)