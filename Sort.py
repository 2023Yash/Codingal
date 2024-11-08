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
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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

    return printer()

printer()