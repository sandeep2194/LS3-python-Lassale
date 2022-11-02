nums = []
count = 0


def findMax(arr):
    max = 0
    for x in arr:
        if (x > max):
            max = x
    return max


while count < 3:
    userInput = float(input('Enter a float value: '))
    if (isinstance(userInput, int)):
        print('***YOur Value is not correct try again****')
    nums.append(userInput)
    count += 1

print('the max is : ', findMax(nums))
