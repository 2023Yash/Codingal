def is_sorted(arr):
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        if(arr[i] > arr[i + 1]):
            return False
    
    return True

def bubble_sort(arr):
    arr_len = len(arr)

    while(not(is_sorted(arr))):
        for i in range(0, arr_len - 1):
            if(arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)

arr = [5, 2, 7, 8, 2, 6, 4]

bubble_sort(arr)