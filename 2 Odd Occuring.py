def Two_Occring_Number():
    n = int(input("Enter array size:"))
    num_list = list()
    preserved_n = n

    while(n):
        inp = int(input("Enter a number"))
        num_list.append(inp)
        n -= 1

    ans = num_list[0]

    x = 0
    y = 0

    Set_Bit = 0

    for i in range(1, preserved_n):
        ans ^= num_list[i]

    Set_Bit = ans &~ (ans - 1)

    for i in range(preserved_n):
        if (Set_Bit & num_list[i]):
            x = x ^ num_list[i]
        else:
            y = y ^ num_list[i]

    print(f"Odd number are {x} and {y}.\n")

    return Two_Occring_Number()

Two_Occring_Number()