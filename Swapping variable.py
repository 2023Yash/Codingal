a = 10
b = 5

def Swap_Method_1 (a=7, b=5):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

print(Swap_Method_1(a, b))

def Swap_Method_2 (a=7, b=5):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    return a, b

print(Swap_Method_2(a, b))