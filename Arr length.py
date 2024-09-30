def recursive_length(arr):
    if arr == []:
        return 0
    
    return 1 + recursive_length(arr[1:])

array = [1, 2, 3, 4, 5]
print("Length of the array:", recursive_length(array))