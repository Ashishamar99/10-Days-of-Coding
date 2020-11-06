matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(len(matrix)):
	print(matrix[i][i]**2, end=" ")
print()
for i in range(len(matrix)):
	print(matrix[i][len(matrix)-i-1]**2, end=" ")

"""
------------------------------------------------------------------------------------------
for i in range(len(matrix)):
	for j in range(len(matrix)):
		if i == j: print(matrix[i][j]**2, 'Primary Diag')
		if ((i>j) and (j==0)) or ((j>i) and (i==0)): print(matrix[i][j]**2, 'Secondary Diag')
		if (i-j == 1) or (j-i == 1): print(matrix[i][j]**2, 'Secondary Diag')

Gives output as ->
1 Primary Diag
4 Secondary Diag
4 Secondary Diag
9 Secondary Diag
16 Secondary Diag
16 Secondary Diag
25 Primary Diag
36 Secondary Diag
49 Secondary Diag
64 Secondary Diag
81 Primary Diag

Solution is a subset of this, formula for secondary diagonal needs to be updated.
------------------------------------------------------------------------------------------
Time complexity = O(n^2)
diag1 = []
diag2 = []
for i in range(len(matrix)):
	for j in range(len(matrix)):
		if i==j: diag1.append(str(matrix[i][j]**2))
		if i+j == len(matrix)-1: diag2.append(str(matrix[i][j]**2))
print(' '.join(diag1))
print(' '.join(diag2))
-------------------------------------------------------------------------------------------
"""