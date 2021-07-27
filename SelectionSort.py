arr = [3, 2, 1, 5, 7]


def Selection(arr):
    for i in range(0, len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        swap(arr, i, m)


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


Selection(arr)
print(arr)
