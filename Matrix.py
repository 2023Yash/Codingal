def adder():
    arr1 = [[2, 4],
            [4, 2]]
    
    arr2 = [[4, 2],
            [2, 4]]
    
    answer = [[0, 0],
              [0, 0]]
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    print(answer)

adder()

def multiplier():
    arr1 = [[8, 2],
            [4, 1]]
    
    arr2 = [[3, 8],
            [9, 15]]
    
    answer = [[0, 0],
              [0, 0]]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    print(answer)

multiplier()