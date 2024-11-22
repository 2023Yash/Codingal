def kadene_algorithm(arr):
    maximum = 0
    cmax = 0

    arr_size = len(arr)

    for i in range(arr_size):
        cmax = cmax + arr[i]

        if(maximum < cmax):
            maximum = cmax

    return cmax

def circullar_sum(arr):
    arr_len = len(arr)
    
    max_kadene = kadene_algorithm(arr)
    max_wrap = 0

    for i in range(0, arr_len):
        max_wrap += arr[i]

        arr[i] = -arr[i]

    max_wrap += kadene_algorithm(arr)

    if(max_wrap > max_kadene):
        return max_wrap
    else:
        return max_kadene

arr = [4, 6, 9, 2, 0]

print(circullar_sum(arr))