def Profit_Loss(arr):
    arr_size = len(arr)

    profit = 0
    for i in range(1, arr_size):

        if arr[i] > arr[i - 1]:

            profit += arr[i] - arr[i - 1]
        
    return profit

arr = [20, 10, 1000, 2000, 1234]

print(Profit_Loss(arr))