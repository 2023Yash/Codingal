def naive(Arr, n, x):
    for i in range(n):
        for j in range(n):
            if(i == j):
                continue

            if(Arr[i] + Arr[j] == x):
                return Arr[i], Arr[j]
            
            if(Arr[i] + Arr[j] > x):
                break

    return 0

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(naive(arr, 8, 9))