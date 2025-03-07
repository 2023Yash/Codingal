import time

def rabin_karp(text, pattern, prime=101):
    """Rabin-Karp string matching algorithm."""
    n = len(text)
    m = len(pattern)
    h_pattern = 0
    h_text = 0
    h = 1

    for i in range(m - 1):
        h = (h * prime) % 2**32

    for i in range(m):
        h_pattern = (prime * h_pattern + ord(pattern[i])) % 2**32
        h_text = (prime * h_text + ord(text[i])) % 2**32

    for i in range(n - m + 1):
        if h_pattern == h_text:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            h_text = (prime * (h_text - ord(text[i]) * h) + ord(text[i + m])) % 2**32
            if h_text < 0:
                h_text += 2**32
    return -1

def kmp(text, pattern):
    """Knuth-Morris-Pratt string matching algorithm."""
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

text = "ABABABABABABABABABABBABABABAABABAB"