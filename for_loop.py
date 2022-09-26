

l1=[1,2,3]# list collection
t1=('James','Marry','Mike','Bill')# tuple collection
dict={}# dictionary collection

for item in l1:
    print(item)
print('this is tuple')
print('using break statement causes stop loop and exit from it')
for t in t1:
    if t=='Mike':
        print('Mike is in t1 tuple colleciton.')
        break
    print(t)

l2=[1,2,3,4,5,6,7,8,9,10]
print('using continue statement is same as short circut and igonre just that iteration and goes to the next item')
for i in l2:
    if i==5:
       continue
    print(i)

print('############## Range is a build in object in python to have sequence of numbers ########### ')
r1=range(0,10)
print(type(r1))
print('########### how to use range')
for item in r1:
    print('---> ',item)

print('use range in the loop without variables')
for n in range(-10,0,1):
    print('range using in loop',n)

for n in range(10):
    print('default range function:',n)


matrix=[['aa','bb','cc','dd'],['ee','ff','gg','hh']] # 2*4
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
print(matrix[0][3])
print('Second collection in the outer matrix')
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])
print(matrix[1][3])
print(len(matrix))
for i in [0,1]:    #outer loop

    for j in [0,1,2,3]: #inner loop
       
        print(f'[{i},{j}] --> {matrix[i][j]}')

print('I am out of the loop.with fix size because we know the size of collection')

matrix1=[['aa','bb','cc','dd'],['ee','ff','gg','hh','mm']] # not symmetrix matrix
for i in range(len(matrix1)):#outer loop
    for j in range(len(matrix1[i])): #nested loop
       
        print(f'[{i},{j}] --> {matrix1[i][j]}')

print('I am out of the loop.')

