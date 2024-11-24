def Mersenna_Prime_Number_Miner():
    start = int(input("Write the Starting point:"))
    end = int(input("Write the Ending point:"))
    for i in range(start, end):
        if(i % 2 != 0):
            for j in range(2, i):
                if(i % j == 0):
                    break
            else:
                p = 1
                while (2 ** p - 1) <= i:
                    if (2 ** p - 1) == i:
                        print(i)
                    p += 1

Mersenna_Prime_Number_Miner()