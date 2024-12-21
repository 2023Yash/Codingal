def merge_sort(arr):
    arr_len = len(arr)
    
    if(arr_len > 1):
        mid = arr_len // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        indenter = 0

        while(i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                arr[indenter] = left[i]
                i += 1
            else:    
                arr[indenter] = right[j]
                j += 1

            indenter += 1

        while(i < len(left)):
            arr[indenter] = left[i]
            indenter += 1
            i += 1

        while(j < len(right)):
            arr[indenter] = right[j]
            indenter += 1
            j += 1

def merge_two_sorted_arrays(arr1, arr2):
    combiended_arr = arr1 + arr2
    merge_sort(combiended_arr)
    print(combiended_arr)

arr1 = [18, 35, 74, 45, 56, 47, 3, 49, 98, 92]
arr2 = [65, 17, 34, 98, 83, 99, 64, 95, 42, 62]

merge_two_sorted_arrays(arr1, arr2)