def insertion_sort(Arr):
    arr_len = len(Arr)
    for i in range(1, arr_len):
        key = Arr[i]
        j = i - 1
        while(j >= 0 and key < Arr[j]):
            Arr[j + 1] = Arr[j]
            j -= 1
            Arr[j + 1] = key

    return Arr[-1]

arr = [74, 87, 16, 96, 44, 15, 93, 57, 74, 69]

print(insertion_sort(arr))