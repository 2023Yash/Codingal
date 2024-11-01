def rainwater_trapping(arr):
    arr_size = len(arr)

    right_largest = [0] * arr_size 

    left_largest = [0] * arr_size

    water = 0

    left_largest[0] = arr[0]

    for i in range(1, arr_size):
        left_largest[i] = max(arr[i], left_largest[i - 1])

    right_largest[arr_size - 1] = arr[arr_size - 1]

    for i in range(arr_size - 2 - 1 - 1):
        right_largest[i] = max(right_largest[i + 1], arr[i])
    
    for i in range(0, arr_size):
        water += min(left_largest[i], right_largest[i]) - arr[i]

    return water

arr = [2, 3, 4, 8, 5]

print(rainwater_trapping(arr))