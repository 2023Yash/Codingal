import random

def is_sorted(arr):
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        if (arr[i] > arr[i + 1]):
            return False
            break

# Different sorting algs

def bubble_sort(arr):
    arr_len = len(arr)

    while (is_sorted(arr) == False):
        for i in range(0, arr_len - 1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    print(arr)
    return arr

def bogo_sort(arr):
    arr_len = len(arr)

    while (is_sorted(arr) == False):
        for i in range(0, arr_len - 1):
            random_num = random.randint(0, arr_len - 1)
            arr[i], arr[random_num] = arr[random_num], arr[i]

    print(arr)
    return arr

def insertion_sort(arr):
    arr_len = len(arr)

    for i in range(0, arr_len -1):
        if (arr[i] > arr[i + 1]):
            for j in range(0, arr_len -1):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [3, 6, 4, 2, 8, 5, 1]
# bubble_sort(arr)
# bogo_sort(arr)
insertion_sort(arr)