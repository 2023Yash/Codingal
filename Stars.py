def stairs(s):
    if (s < 0):
        return 0
    if (s == 0):
        return 1
    
    one = 0
    two = 0

    if (s >= 2):
        two = stairs(s - 2)
    
    one = stairs(s - 1)

    return two + one

print(stairs(3))

a=[88,77,55,66,98] 
a.append(35)
print(a)