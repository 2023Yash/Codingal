def EquilibriumPoint(arr):
    arr_len = len(arr)

    for i in range(0, arr_len):
        sum_left = 0
        sum_right = 0

        for j in range(i):
            sum_left += arr[j]

        for k in range(i + 1, arr_len):
            sum_right += arr[k]

        if (sum_left == sum_right):
            return i
            

arr = [4, 0, 2, 1, 1]

print(EquilibriumPoint(arr))