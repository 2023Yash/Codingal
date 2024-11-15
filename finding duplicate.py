def linear_search(arr, x):
    arr_len = len(arr)
    duplicate = 0

    for i in range(arr_len):
        if(duplicate != 2):
            if(arr[i] == x):
                duplicate += 1
        else:
            return "Duplicate Found!"
    else:
        return "Error 404", "Duplicate not found!"
    

arr = [100, 97, 95, 96, 50, 97, 58, 18, 26, 54]

print(linear_search(arr, 97))