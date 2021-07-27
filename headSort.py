arr = [1, 12, 11, 9, 0]


def headAdjuest(arr, arrsize, deep):
    if arr == None and len(arr) < 2:
        return
    m = deep
    lc = deep * 2 + 1
    rc = lc + 1
    if lc < arrsize and arr[lc] > arr[m]:
        m = lc
    if rc < arrsize and arr[rc] > arr[m]:
        m = rc
    if m != deep:
        arr[m], arr[deep] = arr[deep], arr[m]
        headAdjuest(arr, arrsize, m)


def build_headSort(arr):
    for i in range(len(arr) // 2, -1, -1):
        headAdjuest(arr, len(arr), i)


def headSort(arr):
    build_headSort(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        headAdjuest(arr, i, 0)


headSort(arr)
print(arr)
