
print_var='\n\n ******** {0} *********\n'
set1={'one','two','three','three'}
l1=['one','two','three','three']

print(type(set1))
set1.add(4)
set1.remove(4)
print('using pop built-in funciton in set1 value is -->  {0}'.format(set1.pop()))
print(set1)


set2=set([1,2,3,5,6,5,4,3,2,1,'one','two','three','three'])

print(type(set2))
print('lenght of the set after using list: ',len(set2))

print('\n\n difference between discard and remove')
set2.discard(1)

set2.discard(7)
print('\n\n Using remove funciton with raise an error if item doesn\'t belong to the set: ')
# set2.remove(7)
dif_set=set1.difference(set2)

print('\n\n *********Using different() built-in funciton*********\n\n',dif_set)

dif_set=set2.difference(set1)

print('\n\n *********Using different() built-in funciton reverse sets*********\n\n',dif_set)


print(print_var.format(' using isdisjoint()'))

s1=set([4,5,1,2,3])
s2=set([4,5,10])

print(s1.issubset(s2))
print(s2.issubset(s1))

union_set=s1.union(s2)
print(print_var.format('using union()'))
print(union_set)

print(print_var.format('Uisng update()'))

s1.update(set([7,6,9]))
print(s1)
print(s2)
s3=set([6,7])
print(print_var.format('Uisng superset()'))
print(s1.issuperset(s2))

print(print_var.format('Using symmetric_difference() '))
print(s1.symmetric_difference(s2))

print(print_var.format('Using intersection()'))

print(s1.intersection(s2))
print(print_var.format('Using symmetric_difference_update()'))
s2.symmetric_difference_update(s1)
print(s2)

