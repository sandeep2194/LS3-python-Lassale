

#Q4 of assignment 1
n=0
students=dict()
li=[]
while(n <4):
  st_num=int(input("Give studnet number: "))
  name=input("\nGive studnet name: ")
  li.append(st_num)
  students[st_num]=name
  n+=1

print('\n\n******All Student ********\n ')
print(students)

programs={'Science': [], 'Health': []}
programs['Science'].append(students.pop(li[0]))
programs['Science'].append(students.pop(li[2]))
programs['Health'].append(students.pop(li[1]))
programs['Health'].append(students.pop(li[3]))
print('\n\n**After adding student to program dict**\n')
print(programs)
print('\n******** Find student in each program*****\n')
print('\n\t\t1:Science')
print('\t\t2:Health')
num=int(input('Please enter one of the above numbers: '))
if num==1:
    print(programs['Science'])
elif num==2:
    print(programs['Health'])
else:
    print('Your number is not valid')
