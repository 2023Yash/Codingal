def knapsack(w, v, c):
    n = len(w)
    dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    max_value = dp[n][c]
    item_knapsack = []
    j = c
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_knapsack.append(i - 1)
            j -= w[i - 1]
    return max_value, item_knapsack[::-1]
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
c = 10

max_value, item_knapsack = knapsack(w, v, c)
print(max_value)
print(item_knapsack)