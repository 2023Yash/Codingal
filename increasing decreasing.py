def Increasing_decreasing(n, num):
    if(n < 1 or n > num):
        return
    
    print(n)
    Increasing_decreasing(n - 1, num)
    print(n)

Increasing_decreasing(10, 10)