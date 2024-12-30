def rotate_arr(arr):
    inp = int(input("Enter Rotations:"))
    for i in range(0, inp):
        first_element = arr[0]
        arr.pop(0)
        arr.append(first_element)

    return arr

arr = [5, 4, 3, 2, 1]

print(rotate_arr(arr))