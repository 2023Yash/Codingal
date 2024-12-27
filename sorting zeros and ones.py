def is_arr_sorted(arr):
    for i in range(0, len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            return False

def sort_zeros_and_ones(arr):
    while(is_arr_sorted(arr) == False):
        for i in range(0, len(arr) - 1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)
    return arr

arr = [0, 1, 1, 0, 0, 1, 0]

sort_zeros_and_ones(arr)