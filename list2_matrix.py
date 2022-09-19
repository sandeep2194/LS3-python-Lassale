#********** array is the another name of list **************
#multidimentional array(matrix)
# 2-dimentional array.Two dimensional array is an array within another one.

print('********** [[]] ************ (a 2 dimentional array *************')
print('********** [[]] outer brackets represent outer list and inner brackets represent inner list *************')
print('**************** \n 1*3 matrix \n************')
m2=[['Jan','Feb','March']]
print(m2)
print('\n************************************** \n print 2nd item(inner) in 1st item(outer)  \n**************************\n')
print(m2[0][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
'''
next print I added to show the schematic of a matrix of 3(rows) * 3(columns)
however, it is a combination of tabs and new lines in python ;) 
'''
print('\n***************  matrix = [[1,2,3],[4,5,6],[7,8,9]]  *******************************************\n')
print('\t\t __\t\t\t      __\n\t\t|\t1\t2\t3\t|\n\t\t|\t4\t5\t6\t|\n\t\t|\t7\t8\t9\t|\n\t\t|__\t\t\t      __|\n')
print('\n*********************************************************************************************\n')
print(matrix)

print('********** print 1st item of inner list and 1st item of outer list *************')
print(matrix[0][0])


print('\n********** print all item of inner list and 1st item of outer list *************')
print(matrix[0][:])
print('\n********** print all item of inner list and 2nd item of outer list *************')
print(matrix[1][:])
print('\n********** print all item of inner list and 3rd item of outer list *************')
print(matrix[2][:])

print('\n********** another example(inter list from 0 to 2nd item) *************')
print(matrix[2][:2])