def Mean(arr, arr_len):
    Sum = 0

    for i in range(0, arr_len):
        Sum += arr[i]
    
    Mean = Sum / arr_len

    return Mean

def Median(arr, arr_len):
    sorted(arr)

    if arr_len % 2 == 0:
        return (arr[int(arr_len / 2)] + arr[int(arr_len - 1 / 2)]) / 2
    else:
        return arr[int(arr_len / 2 )]
    
arr = [1, 3, 2, 9]
arr_len = len(arr)

print(Mean(arr, arr_len))
print(Median(arr, arr_len))
