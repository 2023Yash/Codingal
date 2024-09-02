def Counting_0s_And_1():
    n = int(input("Enter a number:"))
    Preserved_n = n

    zero = 0
    one = 0

    while(n):
        if(n&1 == 1):
            one += 1
        else:
            zero += 1
        n >>= 1

    else:
        print(f"In the Binary value of number {Preserved_n} there are {zero} zeros and {one} ones.")

    return Counting_0s_And_1()

Counting_0s_And_1()