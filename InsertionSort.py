arr = [3, 2, 1, 5, 7]


def Selection(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            while j >= 0 and arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


Selection(arr)
print(arr)
