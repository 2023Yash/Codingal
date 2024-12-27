def is_sorted(arr):
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        if (arr[i] > arr[i + 1]):
            return False
        
arr = [8, 4, 5, 9, 6, 1, 2]

print(is_sorted(arr))