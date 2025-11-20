def subset_sum(arr, K):
    n = len(arr)
    result = []

    def backtrack(i, current_sum, subset):
        if current_sum == K:
            result.append(subset[:])
            return True        
        if i >=n or current_sum > K:
            return False
        subset.append(arr[i])
        if backtrack(i + 1, current_sum + arr[i], subset):
            return True        
        subset.pop()
        return backtrack(i+ 1, current_sum, subset)

    backtrack(0, 0, [])

    if result:
        print(result[0])
    else:
        print("No subset found with sum", K)
    

if __name__ == "__main__":
    arr = [3, 34,4, 12, 5, 2]
    K = 9
    subset_sum(arr, K)