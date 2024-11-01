def Array_Reverser(l):
    l_len = len(l)
    
    for i in range(l_len // 2):
        l[i], l[l_len - i - 1] = l[l_len - i - 1], l[i]

arr = [1, 2, 3, 4, 5]

Array_Reverser(arr)

print(arr)
