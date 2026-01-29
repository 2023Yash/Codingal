def min_coin(coin, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coins in coin:
        for val in range(coins, target + 1):
            dp[val] = min(dp[val], dp[val - coins] + 1)

    print(dp[target])

coin = [1, 2, 5, 10]
t = 23
min_coin(coin, t)