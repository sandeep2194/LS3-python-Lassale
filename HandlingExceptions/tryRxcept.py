
# try:
#     while True:
#         X = 1
# except KeyboardInterrupt as e:
#     print("i am cute")


try:
    while True:
        X = int(input('Please enter a int value: '))
except ValueError as e:
    print('\n\n**************************************')
    print(e)
    print('******************************************')
except:
    print('\n\nsomething went wrong!')
