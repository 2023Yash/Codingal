def Four_Power_Check():
    n = int(input("Enter a number:"))

    def Yes():
        print(f"{n} is the power of 4\n")

    def No():
        print(f"{n} is not the power of 4\n")
    
    if (n & n - 1 == 0):
        if (n == 1):
            Yes()
        elif (n % 10 == 4 or n % 10 == 6):
            Yes()
        else:
            No()
    else:
        No()

    return Four_Power_Check()

Four_Power_Check()