def leader(arr):
    arr_len = len(arr)

    leader = arr[arr_len - 1]

    for i in range(arr_len - 2, -1, -1):
        if (arr[i] > leader):
            leader = arr[i]

    return leader

arr = [1, 0, 3, 6, 0, 0, 0, 2, 355, 0, 72]

print(leader(arr))