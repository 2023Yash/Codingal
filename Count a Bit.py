def Count_A_Bit():
    n = int(input("Enter a number:"))
    Preserved_N = n

    count = 0

    while (n):
        count += 1
        n >>= 1

    print(f"Ther are {count} number of bit in the number {Preserved_N}.")

    return Count_A_Bit()

Count_A_Bit()