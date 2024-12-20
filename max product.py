def find_max_product_pair(arr):
    arr.sort()
    max_product = max(arr[0] * arr[1], arr[-1] * arr[-2])

    return max_product

arr = list(map(int, input("Enter the array elements separated by space: ").split()))

result = find_max_product_pair(arr)
print("The maximum product of two elements is:", result)
