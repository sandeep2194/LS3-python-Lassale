

"""
    Operators in Python
    Date: 07 Sep 2022
    Author: Omid
"""
### castin data types
price = 19.99
print(price)
print(type(price))


price_int = int(price)
print(price_int)
print(type(price_int))

age = 23
print(age)
print(type(age))

age_float = float(age)
print(age_float)
print(type(age_float))

"""
name = "Sam"
num = int(name)
print(num)
print(type(num))
"""

num_str = '123'
num_int = int(num_str)
print(num_int)
print(type(num_int))


#### Comparison OPerators
num1 = 21 ## Assignment Operator
num2 = 10
num3 = 0
print("+++++++++++ Comparison OPerators")
print(num1 == num2)
print(num1 != num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 > num2)
print(num1 >= num2)

print("+++++++++++ Math Operators")
### Math Operators
print("num1 + num2 =  ", num1 + num2)
print("num1 - num2 =  ", num1 - num2)
print("num1 * num2 =  ", num1 * num2)
print("num1 / num2 =  ", num1 / num2) ## normal division
print("num1 %% num2 =  ", num1 % num2)
print("num1 // num2 =  ", num1 // num2) ### floor division
print("num1 ** num2 =  ", num1 ** num2) ## 21 pow 10

print("+++++++++++ Assignment Operators")
### Assignment Operators
"""
print(num1)
print(id(num1))
num1 = num1 + num2
print(num1)
print(id(num1))

print(num1)
print(id(num1))
num1 += num2
print(num1)
print(id(num1))
"""

num1 += num2
print("num1 += num2 =  ", num1 )
num1 -= num2
print("num1 -= num2 =  ", num1)
num1 *= num2
print("num1 *= num2 =  ", num1)
num1 /= num2
print("num1 /= num2 =  ", num1) ## Assignment normal division
num1 %= num2
print("num1 %= num2 =  ", num1) ### 21 / 10 = 1 --> num1 =1
num1 //= num2
print("num1 //= num2 =  ", num1) ### 1 // 10 --> num1 = 0
num1 **= num2
print("num1 **= num2 =  ", num1) ## 0 pow 10


print("+++++++++++ Logical Operators")
### Logical Operators

yes = True
no = False

print('yes and no --> ', yes and no)
print('yes and yes --> ', yes and yes)

print('yes or no --> ', yes or no)
print('yes or yes --> ', yes or yes)

print('not yes --> ', not yes)
print('not no --> ', not no)
