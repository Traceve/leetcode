# -*- coding: utf-8 -*-
def quick_sort_standord(array, low, high):
    if low < high:
        key_index = partion(array, low, high)
        quick_sort_standord(array, low, key_index)
        quick_sort_standord(array, key_index + 1, high)


def partion(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low


if __name__ == '__main__':
    array = [9, 3, 2, 1, 4, 6, 7, 0, 5]

    print(array)
    quick_sort_standord(array, 0, len(array) - 1)
    print(array)
