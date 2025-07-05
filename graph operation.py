def min_swaps(arr):
    n = len(arr)
    arr_pos = [(value, idx) for idx, value in enumerate(arr)]
    arr_pos.sort()
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or arr_pos[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1

        if cycle_size > 1:
            swaps += (cycle_size - 1)
    
    return swaps


arr = [4, 3, 2, 1]
print("Minimum swaps required:", min_swaps(arr))
