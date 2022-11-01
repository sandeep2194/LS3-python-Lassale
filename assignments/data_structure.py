

data_structure=((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,16))
row=int(input('Please Enter your first number: '))
collumn=int(input('Please Enter your second number: '))

print('**** your result is {0}   *********'.format(data_structure[row-1][collumn-1]))
i=0
while(i<4):
    j=0
    while(j<4):
        print('\t{0}'.format(data_structure[i][j]),end='')
         # or
        # print(f'\t{data_structure[i][j]}',end='')
        j+=1
    print()
    i+=1
    