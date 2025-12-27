def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

coins = [20, 10, 5, 2, 1]
amount = 21

result = min_coins(coins, amount)
print(result)

# def Min_coins(amount):
#     a = amount
#     n = 0

#     i = (a - (a % 20)) / 20
#     n += i
#     print("20 rupees coins:", i)
#     a = a % 20
#     i = (a - (a % 10)) / 10
#     n += i
#     print("10 rupees coins:", i)
#     a = a % 10
#     i = (a - (a % 5)) / 5
#     n += i
#     print("5 rupees coins:", i)
#     a = a % 5
#     i = (a - (a % 2)) / 2
#     n += i
#     print("2 rupees coins:", i)
#     a = a % 2
#     i = (a - (a % 1)) / 1
#     n += i
#     print("1 rupees coins:", i)
#     print(n)

# Min_coins(31)