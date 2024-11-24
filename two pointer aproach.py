def two_pointer(Arr, x):
    n = len(arr)
    i = 0
    j = n - 1

    while(i < j):
        if(Arr[i] + Arr[j] == x):
            return Arr[i], Arr[j]
        
        elif(Arr[i] + Arr[j] > x):
            j -= 1

        else:
            i += 1

    return f"Elements that when added makes {x} were not found in list {Arr}"

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(two_pointer(arr, 12))