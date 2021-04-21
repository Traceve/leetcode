arr =[7,5,1,10,21]
def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
def swap(arr,i,j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
bubbleSort(arr)
print(arr)
