def more01(arr):
    arr_len = len(arr)
    zeros = 0
    ones = 0
    for i in range(arr):
        if (arr[i] == 0):
            zeros += 1
        else:
            ones += 1

    if (zeros > ones):
        print([1 * arr_len])