matrix = [[1, 2, 4],
          [5, 9, 0],
          [3, 1, 7]]

"""
4x4 matrix ->

matrix = [[1, 2, 4, 11],
          [5, 9, 0, 12],
          [3, 1, 7, 13],
          [6, 8, 10, 14]]
"""

n = len(matrix)
if n==len(matrix[0]): # Checking if given matrix is a square matrix.
    result = matrix.copy()
    for i in range(n):
        for j in range(n):
            if i==j: pass
            elif j > i:
                result[i][j], matrix[j][i] = matrix[j][i], result[i][j]

    print(result)
else:
    print('Not a Sqaure Matrix.')