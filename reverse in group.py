def Arr_Reverse(arr, arr_size, n):
    temp = 0

    while (temp < arr_size):

        start = temp
        end = min(temp + n - 1, arr_size - 1)

        while (start < end):
            arr[start], arr[end] = arr[end], arr[start]

            start += 1
            end -= 1
        
        temp += n

arr = [1, 5, 2, 8, 9, 4]
arr_size = len(arr)
n = 3

Arr_Reverse(arr, arr_size, n)

for i in range(0, arr_size):
    print(arr[i], end=" ")