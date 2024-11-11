def subarraysumn(arr, goal):
    arr_len = len(arr)
    target = arr
    ans = 0

    for i in range(arr_len - 1):
        if arr[i] > goal:
            target.pop(i)

    for i in range(arr_len):
        if((arr[i] + arr[i + 1]) < goal):
            ans += arr[i]
        else:
            break

    return ans

arr = [5, 2, 3, 7, 69, 0]
goal = 10

print(subarraysumn(arr, goal))