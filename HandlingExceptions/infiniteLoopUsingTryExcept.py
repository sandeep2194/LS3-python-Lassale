import sys


def check():
    try:
        while True:
            x = int(input('To exit type 0: '))
            if (x == 0):
                sys.exit()
    except ValueError as err:
        print(err)
        check()
    except SystemExit as err:
        print(err)
    finally:
        print('Bye bye kukur')


check()
