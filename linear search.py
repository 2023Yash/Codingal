def linear_search(arr, x):
    arr_len = len(arr)

    for i in range(arr_len):
        if (arr[i] == x):
            return i
    else:
        return "Error 404", "Element not found!"
    

arr = [31, 72, 57, 56, 32, 79, 94, 63, 79, 18]

print(linear_search(arr, 57))