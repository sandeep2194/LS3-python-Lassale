
'''
continue with operator
1- input function
2- bitwise
3- string with sequences

Author : Omid Panahi
Date    sep 12, 2022
'''
print('********** interactive session with user **********************')
value_from_user = input('Please enter a number:')

print(value_from_user)

print(type(value_from_user))

print('********** convert variables(casting) *************')
convert_value=float(value_from_user)
print('this is casting(convert variable): ', convert_value )

print('short way to convert values')
value_from_user= int(input('PLease, Enter an Integer value: '))
print(type(value_from_user))





print('*********** BITWISE operators *******************')

a=64 # 01000000 (2 to the power of 6)

print(' if we use shift to the left one time it means we multiply that value by 2')
print(' if we use shift to the rith one time it means we devide that value by 2')

print(' shift to the right >>')
print(a)    #  01000000    64
print(a>>1) #  00100000    32
print(a>>2 )#  00010000    16
print(a>>3 )#  00001000    8
print(a>>4 )#  00000100    4
print(a>>5 )#  00000010    2
print(a>>6 )#  00000001    2
print(a>>7 )#  00000000    0
print(' shift to the left <<')

b=1 #          00000001    1     
print(b)   
print(b<<1 )#  00000010    2
print(b<<2 )#  00000100    4
print(b<<3 )#  00001000    8
print(b<<4 )#  00010000    16
print(b<<5 )#  00100000    32
print(b<<6 )#  01000000    64
print(b<<7 )#  10000000    128


print('********** and/or bitwise operators ***************')
print('********** bitwise 60 & 13 ***************')
first_value=60  # 0011 1100
second_value=13 # 0000 1101
#               ------------ and 
#                 0000 1100 

print(first_value & second_value)

print('********** bitwise 60 | 13 ***************')
first_value=60  # 0011 1100
second_value=13 # 0000 1101
#               ------------ or 
#                 0011 1101 

print(first_value | second_value)

print('********** bitwise 60 | 13 ***************')
# 0011 1100
# 0000 1101
#------------ Xor 
# 0011 0001 
print('********** bitwise 60 ^ 13 ***************')
print(first_value ^ second_value)

print( ' how to show negative values(complimentary ')
print(~first_value)

# print(' logical operators')
# A=True   # 1
# B=False   # 0
# print(A and B)


# a list is a series of elements and we have access to each element with [element_index]
str_1='My name is Smith'

print(str_1[0])
print(str_1[1])

in_operator = '*' in str_1
not_in_operator = '*' not in str_1
print(type(in_operator))
print('result of in operator :' , in_operator)

print('result of not in operator :' , not_in_operator)




#   indexes  0  1  2   3  4
number_list=[10,20,30,40,50]

print(number_list[4])
number_list_another=[10,20,30,40,50]

point_number_list=number_list # copy the address of the memory for number_list

print('point_number_list: ',type(point_number_list))
print('diffrent address in the memory :' , number_list_another is number_list)
print('pointer to the same address: ',number_list is point_number_list)




print(' how to tell python to start our program if we do not want to start from the first line')
if __name__ == "__main__":
    print("Hello, World!")














