# recution
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)

print(factorial(5))

# dynamic
def dyn_factorial(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]
    
    return dp[n]

print(dyn_factorial(5))