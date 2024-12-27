def is_sorted(arr):
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        if (arr[i] > arr[i + 1]):
            return False

def bubble_sort(arr, temp):
    arr_len = len(arr)

    while (is_sorted(arr) == False):
        for i in range(0, arr_len - 1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                temp[i], temp[i + 1] = temp[i + 1], temp[i]

    temp.reverse()

    
    return temp

def Largest_Possible_Number(arr):
    temp_arr = list()
    
    for i in range(len(arr)):
        temp_arr.append(int(str(arr[i])[0]))

    bubble_sort(temp_arr, arr)

    Ans = ""

    for i in range(len(arr)):
        Ans += str(arr[i])

    return Ans

arr = [32, 9, 1]
print(Largest_Possible_Number(arr))