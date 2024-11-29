Max_Value = 99999999999999999

def closest_sum_finder(arr, x):
    n = len(arr)

    res_l = res_r = 0

    l = 0
    r = n - 1
    diff = Max_Value
    while(r > l):
        if(abs(arr[l] + arr[r] - x) < diff):
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if(arr[l] + arr[r] > x):
            r -= 1
        else:
            l += 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(closest_sum_finder(arr, 19))