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

    print(arr)
    return arr

def comparison_between_two_arrays(arr1, arr2):
    combiend_arr = arr1 + arr2
    new_combiend_arr = []
    for i in combiend_arr:
        if i not in new_combiend_arr:
            new_combiend_arr.append(i)

    print(merge_sort(new_combiend_arr))


arr1 = [5, 8, 1, 1, 4, 7, 9, 3, 7, 6]
arr2 = [8, 3, 7, 6, 9, 9, 1, 5, 9, 4]
comparison_between_two_arrays(arr1, arr2)