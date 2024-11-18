def binary_search(arr, target):
    arr_len = len(arr)
    l = 0
    r = arr_len - 1
    while(l <= r):
        arr_mid = l + (r - l) // 2
        if (arr[arr_mid] == target):
            return arr_mid
        elif (arr[arr_mid] < target):
            l = arr_mid + 1
        else:
            r = arr_mid - 1

def binary_search_with_recursion(arr, target, l, r):
    arr_len = len(arr)
    if (r >= l):
        arr_mid = l + (r - l) // 2
        if (arr[arr_mid] == target):
            return arr_mid
        elif (arr[arr_mid] < target):
            return binary_search_with_recursion(arr, target, arr_mid + 1, r)
        else:
            return binary_search_with_recursion(arr, target, l, arr_mid - 1)

arr = []
for i in range(0, 10000):
    arr.append(i)
else:
    print(arr)

print(binary_search(arr, 7998))
print(binary_search_with_recursion(arr, 7567, 0, 7567))
