
from functools import reduce


def info():
    print(f'I am here and my __name__ value is --->{__name__}')


if __name__ == '__main__':
    print('m1.py modlue has been run as an entry ')
    info()


list1 = []
count = 0
while count < 4:
    x = float(input("Enter a float number:"))
    count += 1
    if isinstance(x, float):
        list1.append(x)
    else:
        print("* YOUR VALUE IS NOT CORRECT TRY AGAIN **")


def largest_number(x, y):
    if x < y:
        return y
    else:
        return x


biggest_number = reduce(largest_number, list1)
print(biggest_number)
