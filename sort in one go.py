def Swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]

def Sort(arr):
    arr_len = len(arr)

    if (arr_len <= 1):
        return arr
    
    x = -1
    global y
    y = -1
    previous = arr[0]

    for i in range(1, len(arr)):
        if (previous > arr[i]):
            if (x == -1):
                x = i - 1
                y = i
            else:
                y = i
        previous = arr[i]

    Swap(arr, x, y)

arr = [3, 5, 6, 9, 8, 7]

Sort(arr)

print(arr)