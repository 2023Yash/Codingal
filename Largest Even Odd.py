def longest_subarray_same_ends(arr):
    positions = {}
    
    for i, num in enumerate(arr):
        if num not in positions:
            positions[num] = [i, i]
        else:
            positions[num][1] = i
    
    max_length = 0
    for first, last in positions.values():
        max_length = max(max_length, last - first + 1)
    
    return max_length

a = [6, 4, 9, 4, 7, 2, 3, 4, 2, 52]

print(longest_subarray_same_ends(a))
