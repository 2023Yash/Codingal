def LCS(x, y, m, n):
    table = [[None] * (n + 1) for i in range (m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    
    return table[m][n]

str1 = "Burger"
str2 = "Ginger"
m = len(str1)
n = len(str2)
print(LCS(str1, str2, m, n))

def LCS1 (str1, str2):
    m = len(str2)
    n = len(str1)
    dp = [[0] * (n+1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i -1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j -1]+1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(type(lcs_str))
    return lcs_str

str1_1 = "Burger"
str2_1 = "Ginger"
print(LCS1(str1_1, str2_1))