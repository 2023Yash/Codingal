fac_i = 0

def fac(n):
    global fac_i
    
    if n == 1 or n == 0:
        fac_i += 1
        return 1

    fac_i += 1
    return n * fac(n - 1)

fac(10)
print(fac_i)
# n = fac_i so, time comlexity = O(n) 

print1to10_i = 0

def print1to10(n):
    global print1to10_i
    
    if n > 10:
        print1to10_i += 1
        return

    print(n)
    
    print1to10(n + 1)

print1to10(10)
print(print1to10_i)
# n = print1to10_i so, time comlexity = O(1) 
