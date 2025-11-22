def sub_word_check(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]

dictionary = ["app", "lied"]
string = "applied"

if sub_word_check(string, dictionary):
    print("Sub words found")
else:
    print("No sub words")