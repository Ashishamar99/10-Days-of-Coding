n = int(input('n = '))
matrix = []
for i in range(n):
    row = input(f'Enter row {i} elements seperated by a single space= ')
    row = [int(j) for j in row.split(' ')]
    matrix.append(row)

product_list = []

for row in matrix:
    res = 1
    for i in row: res *= i
    product_list.append(res)
    
for i in range(n):
    res = 1
    for j in range(n): res *= matrix[j][i]
    product_list.append(res)

print(max(product_list))