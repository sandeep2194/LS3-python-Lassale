d1={}
print(type(d1))
d2={1:'Montreal',2:'Toronto',3:'Ottowa',4:'Mntreal',5:'Toronto',6:'Ottowa'}
print(d2)
print(d2)
print(len(d2))
 
populations={'Montreal':4000000,'Toronto':7000000,'Ottowa':1000000}
 
print(populations['Montreal'])
pop2={'canada':{'Montreal':4000000,'Toronto':7000000,'Ottowa':1000000},
    'US':{'Newyork':2000000,'Orlando':4000000,'San Fransico':11000000}}
 
print('\Get US dictionary from pop2 ')
us_dict=pop2['US']
 
print('\nprint a key in us_dict')
print(us_dict['Orlando'])
 
print('\nSame is the above example')
print(pop2['US']['Orlando'])
 
from operator import ne
 
 
software=['scripting','C#','Modeling']
networking=['Cloud computing','Linux','Vritualization']
art=['music','sport']
 
programs={'Software':['scripting','C#','Modeling'],
                'networking':['Cloud computing','Linux','Vritualization'],
                'art':['music','sport']}
 
lasalle_college={'Software':software,
                'networking':networking,'art':art}
## use items and not variales
software.append('python2')
software.extend(networking)
print(programs)
 
# using variables
 
print(lasalle_college)
print(lasalle_college.keys())
print(lasalle_college.values())
print(d2.values())