import random

def is_sorted(arr):
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        if (arr[i] > arr[i + 1]):
            return False

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

    return printer()

printer()