def Second_Largest_Number(arr, size):
    largest = Second_Largest = 0

    for i in range(size):
        if (arr[i] > largest):
            Second_Largest = largest
            largest = arr[i]
        elif (arr[i] > Second_Largest and arr[i] != largest):
            Second_Largest = arr[i]

    print(Second_Largest)

a = [1, 3, 4, 2, 9]
size = len(a)
Second_Largest_Number(a, size)