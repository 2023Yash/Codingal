def most_conscecutive(arr):
    arr_len = len(arr)

    counter = 0
    most_ones = 0

    for i in range(arr_len):
        if (arr[i] == 0):
            counter = 0
        else:
            counter += 1
            most_ones = max(most_ones, counter)
    
    return most_ones

arr = [1, 1, 1, 0, 0, 0, 1]

print(most_conscecutive(arr))