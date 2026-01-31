import sys

def MatrixOrder(p, i, j):
    if i == j:
        return 0
    
    minimum = sys.maxsize

    for k in range(i, j):
        count = (MatrixOrder(p, i, k) + MatrixOrder(p, k + 1, j) + p[i - 1] * p[k] * p[j])

    if count < minimum:
        minimum = count

    print(minimum)

arr = [1, 2, 3, 4, 5]
n = len(arr)

MatrixOrder(arr, 1, n - 1)