def nearest_sum_pair(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    closest_sum = float('inf')
    closest_pair = None
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            closest_pair = (arr[left], arr[right])
        
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            break
    
    return closest_pair, closest_sum

arr = [10, 22, 28, 29, 30, 40]
target = 54
pair, sum_value = nearest_sum_pair(arr, target)
print(f"Closest pair: {pair}, Sum: {sum_value}")
