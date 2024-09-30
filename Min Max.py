def Min_Max(arr):
    if (len(arr) == 1):
        return arr[0]
    if (len(arr) == 0):
        return
    return max(arr[0], Min_Max(arr[1:]))

array = [1, 2, 6, 5, 2]
print(Min_Max(array))