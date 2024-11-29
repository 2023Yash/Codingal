def Smallest_Missing_Element(arr):
    for i in range(0, len(arr) - 1):
        left = arr[i]
        right = arr[i + 1]
        if(right - left != 1):
            return left + 1
        
arr = [1, 2, 3, 4, 6, 7]

print(Smallest_Missing_Element(arr))