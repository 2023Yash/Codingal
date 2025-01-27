import random

def rev_string(string):
    li = list(string)
    length = len(li)
    for i in range(length // 2):
        li[i], li[length - i - 1] = li[length - i - 1], li[i]
    return "".join(li)

string = "Yash Naudiyal"
print(rev_string(string))

def random_string_slicer():
    num_str = "0123456789"
    print()
    print(f"Orignal string:{num_str}")

    r1 = random.randint(1, 9)
    r2 = random.choice([i for i in range((r1 + 1), 10)])
    print(f"Sliced string:{num_str[r1:r2]}, r1 = {r1}, r2 = {r2}")
random_string_slicer()