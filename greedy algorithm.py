def print_max(s, f):
    n = len(f)
    i = 0
    print(i, end=" ")
    for j in range(1, n):
        if s[j] >= f[i]:
            print(j, end=" ")
            i = j
if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]

print_max(s, f)