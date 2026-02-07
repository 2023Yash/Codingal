def palindrome(s):
    return s == s[::-1]

def palindrome_partitioning(s):
    n = len(s)
    dp = [float('inf')] * n

    for i in range(n):
        for j in range(i + 1):
            if palindrome(s[j:i + 1]):
                if i == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
    
    print(dp[n - 1])

string = "aabcb"
palindrome_partitioning(string)