# functions for sorting algothrithms

import random

def is_sorted(arr):
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        if (arr[i] > arr[i + 1]):
            return False

def pi(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if(arr[j] <= pivot):
                i += 1
                arr[j], arr[i] = arr[i], arr[j]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

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
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(arr)
    return arr

def selection_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        I = i
        for j in range(i + 1, arr_len):
            if(arr[I] > arr[j]):
                I = j
        arr[i], arr[I] = arr[I], arr[i]

    print(arr)
    return arr

def shell_sort(arr):
    arr_len = len(arr)

    interval = arr_len // 2
    while(interval > 0):
        for i in range(interval, arr_len):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2

    print(arr)
    return arr

def quick_sort(arr, low, high):
    if(low < high):
        pi_var = pi(arr, 0, high)
        quick_sort(arr, low, pi_var - 1)
        quick_sort(arr, pi_var + 1, high)
    print(arr)
    return arr

def merge_sort(arr):
    arr_len = len(arr)
    
    if(arr_len > 1):
        mid = arr_len // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        indenter = 0

        while(i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                arr[indenter] = left[i]
                i += 1
            else:    
                arr[indenter] = right[j]
                j += 1

            indenter += 1

        while(i < len(left)):
            arr[indenter] = left[i]
            indenter += 1
            i += 1

        while(j < len(right)):
            arr[indenter] = right[j]
            indenter += 1
            j += 1

    print(arr)
    return arr

def printer():
    arr = list()

    arr_length = int(input("Enter array length:"))
    print()

    for i in range(arr_length):
        item_inp = int(input(f"Enter array item no. {i}:"))
        arr.append(item_inp)
    
    print()

    print("Press 1 for bubble sort,")
    print("Press 2 for bogo sort,")
    print("Press 3 for insert sort,")
    print("Press 4 for selection sort,")
    print("Press 5 for shell sort,")
    print("Press 6 for quick sort,")
    print("Press 7 for merge sort,")

    print()

    inp = int(input(":"))

    if (inp == 1):
        print(f"Sorted array is {bubble_sort(arr)}.")
        print()
        print()
        print()
    
    if (inp == 2):
        print(f"Sorted array is {bogo_sort(arr)}.")
        print()
        print()
        print()

    if (inp == 3):
        print(f"Sorted array is {insertion_sort(arr)}.")
        print()
        print()
        print()

    if (inp == 4):
        print(f"Sorted array is {selection_sort(arr)}.")
        print()
        print()
        print()

    if (inp == 5):
        print(f"Sorted array is {shell_sort(arr)}.")
        print()
        print()
        print()
    
    if (inp == 6):
        print(f"Sorted array is {quick_sort(arr, 0, len(arr) - 1)}.")
        print()
        print()
        print()

    if (inp == 7):
        print(f"Sorted array is {merge_sort(arr)}.")
        print()
        print()
        print()

    return printer()

printer()