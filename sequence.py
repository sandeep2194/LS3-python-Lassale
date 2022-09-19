 
'''
string (sequence) functions:
format
upper
lower
find
'''
seq='My name is Smith and family name ?'
upper_seq=seq.upper()
print(upper_seq.lower())
print(upper_seq[:6])
first_name=input('Please enter you first name? ')
last_name=input('Please enter you last name? ')
result ='Your fist name is {0} and your last name is {1}'
result1='your fist name is '+ first_name + ' and your family name is '+ last_name
# print(result)
print(result.format(first_name,last_name,first_name,last_name))
sequence2='Search in the string.... '
print(sequence2.find('r'))
 
number_of_characters=len(sequence2)
number_of_characters='change it'
print(number_of_characters)
print(len(sequence2))
