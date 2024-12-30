def rotate_arr(arr):
    inp = int(input("Enter Rotations:"))
    for i in range(0, inp):
        last_element = arr[-1]
        arr.pop(-1)
        arr.insert(0, last_element)

    return arr

arr = [5, 4, 3, 2, 1]

print(rotate_arr(arr))