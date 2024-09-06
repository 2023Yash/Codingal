def First_set_bit():
    n = int(input("Enter a number:"))

    for i in range(1, n + 1):
        if (n & 1 << (i -1)):
            print(i)
            break

    print()
    
    return First_set_bit()

First_set_bit()