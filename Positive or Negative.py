def Pos_Or_Negative():
    inp = int(input("Enter a number:"))

    if (inp < 0):
        print("Number is negative")
        return
    
    print("Number is Positive")
    return Pos_Or_Negative()

Pos_Or_Negative()