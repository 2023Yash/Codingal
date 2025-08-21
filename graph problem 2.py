def is_sum_string_util(s, start, n1, n2):
    if start == len(s):
        return True
    total = str(n1 + n2)
    l = len(total)
    if start + l > len(s) or s[start:start+l] != total:
        return False
    return is_sum_string_util(s, start + l, n2, int(total))

def is_sum_string(s):
    n = len(s)

    for i in range(1, n):
        for j in range(i+1, n):
            n1 = int(s[:i])
            n2 = int(s[i:j])
            if is_sum_string_util(s, j, n1, n2):
                return True
    return False

print(is_sum_string("122436"))
print(is_sum_string("1111112223"))
print(is_sum_string("1235"))
