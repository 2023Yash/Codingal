def Power_of_4(n):
    if (n == 0):
        return False
    if (n == 1):
        return True
    if (n % 4 == 0):
        return Power_of_4(n / 4)
    
    return False
    
if (Power_of_4(32)):
    print("1024 is power of 4")
else:
    print("1024 is not power of 4")