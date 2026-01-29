def min_jumps(arr):
    n = len(arr)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n - 1]

arr = [2, 3, 9, 7]
print(min_jumps(arr))