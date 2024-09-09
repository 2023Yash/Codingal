def Power_calculator():
    Base = int(input("Enter Base:"))
    Exponent = int(input("Enter Exponent:"))
    Result = 1

    while (Exponent > 0):
        if (Exponent % 2 == 0):
            Base *= Base
            Exponent >>= 1
        else:
            Result *= Base
            Exponent -= 1
    else:
        print(Result,"\n")

    return Power_calculator()

Power_calculator()