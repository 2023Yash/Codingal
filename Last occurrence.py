def Last_occurrence(arr, x):
    arr_len = len(arr)
    ans = 0

    for i in range(arr_len):
        if(arr[i] == x):
            ans = i
            
    return ans

arr = [6, 66, 7, 79, 15, 57, 7, 31, 82, 32]

print(Last_occurrence(arr, 7))