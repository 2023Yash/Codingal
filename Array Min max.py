def Min(arr, arr_len):
    temp = arr[0]

    for i in range(1, arr_len):
        temp = min(temp, arr[i])
    
    return temp

def Max(arr, arr_len):
    temp = arr[0]

    for i in range(1, arr_len):
        temp = max(temp, arr[i])

    return temp

arr = [2, 4, 1, 7, 3]
size = len(arr)

print(Min(arr, size))
print(Max(arr, size))
