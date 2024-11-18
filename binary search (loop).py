def binary_search(arr, target):
    arr_len = len(arr)
    l = 0
    r = arr_len - 1
    l_or_r = 0

    while(l <= r):
        arr_mid = l + (r - l) // 2
        if (arr[arr_mid] == target):
            return arr_mid
        elif (arr[arr_mid] < target):
            l = arr_mid + 1
        else:
            r = arr_mid - 1

arr = [1, 2, 3, 4, 5]


print(binary_search(arr, 4))