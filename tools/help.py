import random


def func2(array):
    if len(array)<=1:
        return array
    tmp = array[0]
    left = [x for x in array[1:] if x<=tmp]
    right = [x for x in array[1:] if x>tmp]
    return func2(left) + [tmp] + func2(right)

def func(array):
    if len(array)<=1:
        return array
    mid = array[random.randint(0,len(array)-1)]
    left = []
    right = []
    for i in range(0,len(array)):
        if array[i] <=mid:
            left.append(array[i])
        else:
            right.append(array[i])
    return func(left)+[mid]+func(right)

if __name__ == '__main__':
    array = [5,4,3,2,1]
    print(func(array))