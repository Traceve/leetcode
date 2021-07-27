import random, operator


def MergeSort(arr, l, r):
    if l == r:
        return
    mid = (l + r) // 2
    MergeSort(arr, l, mid)
    MergeSort(arr, mid + 1, r)
    Merge(arr, l, mid, r)


def Merge(arr, l, mid, r):
    help = [None] * (r - l + 1)
    i = 0
    p1 = l
    p2 = r
    cur = mid + 1
    while p1 <= mid and cur <= r:
        if arr[p1] <= arr[cur]:
            help[i] = arr[p1]
            p1 = p1 + 1
            i = i + 1
        else:
            help[i] = arr[cur]
            cur = cur + 1
            i = i + 1
    while p1 <= mid:
        help[i] = arr[p1]
        p1 = p1 + 1
        i = i + 1
    while cur <= r:
        help[i] = arr[cur]
        cur = cur + 1
        i = i + 1
    for i in range(0, len(help)):
        arr[l + i] = help[i]
        i = i + 1


# 随机产生一组长度为size，数字范围为-value到value
def GenerateRandomArray(size, value):
    array = []
    for i in range(size):
        array.append(int((value + 1) * random.random()) - int(value * random.random()))
    return array


# 创建一个绝对正确的方法,自身的排序算法
def RightMethod(array):
    array.sort()
    return array


def IsRight(times, size, value, func):
    succed = True
    for i in range(times):
        arr1 = GenerateRandomArray(size, value)
        arr2 = arr1.copy()
        arr3 = arr1.copy()
        func(arr1, 0, 9)
        RightMethod(arr2)
        if not operator.eq(arr1, arr2):
            succed = False
            print(arr3)
            break
    print("Nice" if succed == True else "Wrong")


IsRight(5000, 10, 10, MergeSort)
arr = GenerateRandomArray(10, 10)
print(arr)
MergeSort(arr, 0, 9)
print(arr)
