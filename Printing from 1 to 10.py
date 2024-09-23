def Priting_From_1_To_10(n):
    if (n < 1):
        return
    
    Priting_From_1_To_10(n - 1)

    print(n)


Priting_From_1_To_10(10)