def Flip():
    number_1 = int(input("Enter number 1:"))
    number_2 = int(input("Enter number 2:"))

    flip = 0

    while number_1 > 0 or number_2 > 0:
        t1 = number_1 & 1
        t2 = number_2 & 1

        if(t1 != t2):
            flip += 1
        
        number_1 >>= 1
        number_2 >>= 1

    print(flip, "\n")

    return Flip()

Flip()