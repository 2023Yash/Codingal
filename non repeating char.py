def non_repeating_char(s):
    d = {}
    for i in range(len(s)):
        if(s[i] in d.keys()):
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    for i in d:
        if(d[i] == 1):
            print(i)
            break
    else:
        print("no repeating character")
    return d

non_repeating_char("yash Naudiyal")