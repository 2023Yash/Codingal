def Power_Check():
    n = int(input("Enter a number:"))
    ans = 0
    s = 0

    while ans < n:
        ans = 1 << s
        if (ans == n):
            print(f"{n} is a power of 2\n")
            break
        s += 1
    else:
        print(f"{n} is not a power of 2\n")


    return Power_Check()

Power_Check()