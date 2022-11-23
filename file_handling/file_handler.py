import os
path =os.path.dirname(__file__)

f= open(f'{path}\myfile.txt')

print(f.read())
f= open(f'{path}\myfile.txt')
print('Read each line and printout to the console.')
while True: 
   
   line = f.readline()
   print(line)
   if not line:
      break 

f.close()
f= open(f'{path}\myfile.txt','w')

f.write('\nAdd new line to the file')
f.close()

f= open(f'{path}\myfile1.txt','x')

os.remove(f'{path}\myfile1.txt')
    