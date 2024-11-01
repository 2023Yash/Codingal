def find_missing_number(arr):
    n = len(arr) + 1
    sum_of_n = n * (n + 1) // 2
    sum_of_arr = sum(arr)
    missing_number = sum_of_n - sum_of_arr
    return missing_number

arr = [1, 4, 3, 2, 6]
print(find_missing_number(arr))
