def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(arr, k):
    size = len(arr)
    if size == 0:
        arr.append(k)
    else:
        arr.append(k)
        for i in range((size // 2) -1, -1, -1):
            heapify(arr, size, i)

def delete(arr, k):
    size = len(arr)
    i = 0

    for i in range(0, size):
        if k == arr[i]:
            break
    arr[i], arr[size - 1] = arr[size - 1], arr[i]
    arr.remove(k)
    for i in range((size // 2) -1, -1, -1):
        heapify(arr, len(arr), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 6)
insert(arr, 5)
insert(arr, 8)
insert(arr, 2)

print(arr)

delete(arr, 8)

print(arr)