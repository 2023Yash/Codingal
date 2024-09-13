def power_of_eight():
    n = int(input("Enter a number: "))
    original_n = n

    if n > 0:
        while n % 8 == 0:
            n //= 8
    
    if n == 1:
        print(f"{original_n} is a power of 8.")
    else:
        print(f"{original_n} is not a power of 8.")

    return power_of_eight()

power_of_eight()
