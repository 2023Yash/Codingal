def sum_of_row():
    x = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    for i in range(len(x)):
        answer = 0
        for j in range(len(x[0])):
            answer += x[i][j]
        print(answer)

sum_of_row()