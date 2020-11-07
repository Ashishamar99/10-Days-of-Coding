matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == 0: print(matrix[i][j], end=' ')
        if (i != 0) and (i+j == len(matrix)-1) and (i != len(matrix)-1): print(matrix[i][j], end=' ')
        if i == len(matrix)-1: print(matrix[i][j], end=' ')