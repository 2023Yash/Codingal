Max = 100

dp = [[[[-1] * 4 for i in range(Max)] for j in range(Max)] for k in range(Max)]

def counting_ways(p, q, r, last = 1):
    if(p < 0 or q < 0 or r < 0):
        return 0
    
    if(p == 1 and q == 0 and r == 0 and last == 0):
        return 1
    
    if(p == 0 and q == 0 and r == 1 and last == 2):
        return 1
    
    if(last == 0):
        dp[p][q][r][last] = (counting_ways(p - 1, q, r, 0) + counting_ways(p - 1, q, r, 2))
    elif(last == 1):
        dp[p][q][r][last] = (counting_ways(p, q - 1, r, 0) + counting_ways(p, q - 1, r, 2))
    else:
        dp[p][q][r][last] = (counting_ways(p, q, r - 1, 0) + counting_ways(p, q, r - 1, 1))
    
    return dp[p][q][r][last]

p, q, r = 1, 1, 1
print(counting_ways(p, q, r))