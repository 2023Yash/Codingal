def kadene_algorithm(arr):
    maximum = -9999999
    cmax = 0

    arr_size = len(arr)

    for i in range(arr_size):
        cmax = cmax + arr[i]

        if(maximum < cmax):
            maximum = cmax

    return cmax

arr = [4, 6, 9, 2, 0]

print(kadene_algorithm(arr))