import random, operator


def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


# 产生一个随机数列长度的size，数字范围维-value ~ value
def GenerateRandomArray(size, value):
    array = []
    for i in range(size):
        array.append(int((value + 1) * random.random()) - int(value * random.random()))
    return array


# 一定正确的方法，自带排序方法
def RightMathod(array):
    array.sort()
    return array


def IsRight(times, size, value, func):
    succeed = True
    for i in range(times):
        arr1 = GenerateRandomArray(size, value)
        arr2 = arr1.copy()
        arr3 = arr1.copy()
        func(arr1)
        RightMathod(arr2)
        if not operator.eq(arr1, arr2):
            succeed = False
            print(arr3)
            break
    print("Nice" if succeed == True else "WRONG")


arr = GenerateRandomArray(10, 10)
print(arr)
bubbleSort(arr)
print(arr)
IsRight(500000, 10, 100, bubbleSort)
