#Q4
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
# first solution
it=list()
for  v in  speed.items():
    if v[1] in it:
        pass
    else:
        it.append(v[1])
print(it)
#second solution
items=set()
for m in speed.items():
    items.add(m[1])
print(items)

# 3rd solution
result={ v for k,v in speed.items()}
print(result)
print( {v for k,v in speed.items()})

#Q5

statement='I am here and time is 10:02 pm'
res=''
for i in range(len(statement)-1,-1,-1):
     res+=statement[i]
print(res)

def reverse_order_string(statement:str)->str:
    res=''
    for i in range(len(statement)-1,-1,-1):
     res+=statement[i]
    return res
print(reverse_order_string(statement))

#Q6
course_ids=('EL1','EL2','SL3','SL2') 
student_enrollments={'1000-2222':['EL1','SL3'],'2000-1001':['EL1','EL2'],'3000-1234':['SL2'],'1000-1111':['SL3']} 

def find_student_class(ids,enrollments):
    r=dict()
    for id in course_ids:
        st_list=list()
        for st_id,courses in student_enrollments.items():
            if id in courses:
              st_list.append(st_id)  
        r[id]=st_list    
    return r

print(find_student_class(course_ids,student_enrollments))