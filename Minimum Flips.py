def minimum_flips(arr):
    zeros = arr.count(0)
    ones = arr.count(1)
    
    more = 0 
    
    if zeros > ones:
        more = 0
    else:
        more = 1
    
    return [more] * len(arr)

arr = [0, 1, 1]
print(minimum_flips(arr))
