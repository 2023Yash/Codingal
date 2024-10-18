def Rotation(arr, n):
    for i in range(n):
        arr.append(arr[0])
        arr.pop(0)

arr = [1, 2, 3, 4, 5, 6]
n = 2
print(arr)
Rotation(arr, n)
print(arr)