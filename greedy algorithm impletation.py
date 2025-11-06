def Maximum_Activities(arr, n):
    selected = []
    Activity.sort(key= lambda x:x[1])
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j

    return selected

if __name__ == '__main__':
    Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
    n = len(Activity)

    selected = Maximum_Activities(Activity, n)
    print("Selected acticities are:")
    print(selected[0], end=" ")
    for i in range(1, len(selected)):
        print(",", end=" ")
        print(selected[i], end=" ")