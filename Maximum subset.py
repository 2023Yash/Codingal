def max_sum_no_consecutive(arr):
    n = len(arr)

    if n == 0:
        return 0
    elif n == 1:
        return max(0, arr[0])
    
    i1 = max(0, arr[0])
    exc = 0
    
    for i in range(1, n):
        n_i1 = arr[i] + exc
        n_exc = max(i1, exc)
        i1, exc = n_i1, n_exc
    
    return max(i1, exc)

arr = [3, 6, 8, 0]
print(max_sum_no_consecutive(arr))