# empty list
lst=[]
print(type(lst))
number_list=[1,3,4,6,7,9,66.00,'a','string ']
print(number_list)
print(number_list[4:])
print(number_list[:4])
# print(number_list[11]) out of index error.
 
str='a b c d '
lst2=['a','b','c','d','a','b','c','d',49,'it is python program']
 #slice
print(str[0:4])
print(lst2[1:3])
sub_list=lst2[1:3]
print(type(sub_list))
print(' get the list size ')
 # len() function to get the size of the list don't forget it is deferent from list indexes.
print(lst2[7:len(lst2)-1])
 
 
l1=[12,'abc',44.45,'a',True]
print(l1)
# append function adds item to the end of a list
l1.append('new item')
 
print('after append funciton: ',l1)
l1.remove(12)
print('remove',l1)
print('assign value to the list ')
l1[3]=False
print(l1)
print('************* Sort a list **********')
 
num_list=[4,1,-10,66,90]
print('before sort : ',num_list)
num_list.sort()
print('After sort \t',num_list)
num_list.reverse()
print('After call reverse function: \n\n',num_list)
 
ll=[]
ll.append(1)
ll.append(2)


ss=[True,False, False, True]
 ## combine lists to create new list
l3=ll+ss
print(l3)
 
l3.insert(3,'added item')
 
print(l3)
 # get the last item in an array.
print(l3.pop())
print(l3)
 
 
l3.append(ll)
 
print(l3)
# we can use extend(yourlist) function to add to the list 
Listx=['math', 'physics', 'arabic', 'Algebra']
Listx.extend(Listx)
print(Listx)
Listx.extend(["English","chemistry"])

print('using Insert function in the list ')
#END


