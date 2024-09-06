def Odd_1_Out():
    n = int(input("Enter array size:"))
    num_list = list()

    while(n):
        inp = int(input("Enter a number"))
        num_list.append(inp)
        n -= 1

    res = 0

    for i in num_list:
        res = res ^ i
    
    print(f"Odd 1 out in {res}\n")

    return Odd_1_Out()

Odd_1_Out()