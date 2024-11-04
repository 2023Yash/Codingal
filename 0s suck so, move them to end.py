def zeros_suck_so_move_them_to_end(arr):
    arr_length = len(arr)

    new_arr = list()

    zeros = 0

    for i in range(arr_length):
        if(arr[i] == 0):
            zeros += 1
        else:
            new_arr.append(arr[i])

    for i in range(zeros):
        new_arr.append(0)

    return new_arr

arr = [1, 0, 3, 6, 0, 0, 0, 2, 355, 0, 72]

print(zeros_suck_so_move_them_to_end(arr))