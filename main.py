from my_pkg import m1

def check_file(name):
    if name =='__main__':
        print(f'This is an entry point(running python file) ')
    else:
        print(f'__name__ value is --> {name}')

print('Check __name__ value in different python modules')
check_file(__name__)

check_file(m1.__name__)


