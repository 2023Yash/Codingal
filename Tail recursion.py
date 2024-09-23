def Priting_From_1_To_10(n):
    if (n < 1):
        return
    
    print(n)

    Priting_From_1_To_10(n - 1)


Priting_From_1_To_10(10)