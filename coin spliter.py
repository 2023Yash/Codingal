def coin_split(n, coins, index=0, current_combination=None):
    if current_combination is None:
        current_combination = []

    if n == 0:
        print(current_combination)
        return
    
    if index >= len(coins) or n < 0:
        return

    coin_value = coins[index]
    max_coin_count = n // coin_value

    for count in range(max_coin_count + 1):
        new_combination = current_combination + [coin_value] * count
        coin_split(n - coin_value * count, coins, index + 1, new_combination)

coins = [500, 100, 10, 5, 1]
n = 1000

coin_split(n, coins)