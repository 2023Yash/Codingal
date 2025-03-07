def Rabin_karp(pattern, string, q):
    m = len(pattern)
    n = len(string)
    p = 0 
    t = 0
    h = 1
    i = 0
    j = 0

    d = 10

    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (p * d + ord(pattern[i])) % q
        t = (d * t + ord(string[i])) % q
    
    for i in range(m - n + 1):
        if(p == t):
            for j in range(m):
                if(string[i + j] != pattern[j]):
                    break
            j += 1
            if j == m:
                print(f"pattern found ant {i + 1}")
        if (i < n - m):
            t = (d * (t - ord(string[i]) * h) + ord(string[i + m])) % q
            if (t < 0):
                t += q

string = "ABCDEABCDEABCDEABCDEABCDEABCDE"
pattern = "ABCDE"
q = len(string + pattern)


Rabin_karp(pattern, string, q)