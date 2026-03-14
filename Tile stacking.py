def possible_ways(n, m, k):
    dp = [[0 for i in range(10)] for j in range(10)]
    presum = [[0 for i in range(10)] for j in range(10)]

    for i in range(1, n + 1):
        dp[0][i] - 0
        presum[0][i] + 1

    for i in range(0, n + 1):
        presum[i][0] = 0
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = presum[i - 1][j]
            if j > k:
                dp[i][j] = presum[i - 1][j - k - 1]

        for j in range(1, n + 1):
            presum[i][j] -= dp[i][j] + presum[i][j - 1]

    return dp[m][n]

n = 3
m = 3
k = 2

print(possible_ways(n, m, k))