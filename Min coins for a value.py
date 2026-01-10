def Min_coin(m, arr):
    l = len(arr)
    t = m
    ans = 0

    for i in range(0, l):
        if arr[i] > t:
            pass
        else:
            ans += 1
            t -= arr[i]
    print(ans)

t = 14
arr = [1, 2, 5, 10]
Min_coin(t, arr)