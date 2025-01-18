def transposition():
    x = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    answer = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(x)):
        for j in range(len(x[0])):
            answer[i][j] = x[j][i]

    print(answer)

transposition()

def sum_of_columns():
    x = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    for i in range(len(x)):
        answer = 0
        for j in range(len(x[0])):
            answer += x[j][i]
        print(answer)

sum_of_columns()