def rev_string(string):
    li = list(string)
    length = len(li)
    for i in range(length // 2):
        li[i], li[length - i - 1] = li[length - i - 1], li[i]
    return "".join(li)

string = "Yash Naudiyal"
print(rev_string(string))