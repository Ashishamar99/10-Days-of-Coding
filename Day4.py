matrix = [[1, 2, 3, 4, 5],
          [3, 4, 5, 8, 10],
          [3, 5, 7, 9, 11],
          [1, 3, 5, 7, 9]]

n = len(matrix)
sets = []
for i in list(range(n)):
    
    """
    If sets = {}, we can use this approach to name the sets as well.
    my_set = f'set{i}'
    sets[my_set] = set(matrix[i])
    """
    
    sets.append(set(matrix[i]))

intersection_set = set.intersection(*sets)

"""
for num in intersection_set: print(i, end=" ")

The above code prints 3 3 even if intersection_set is {3, 5}
"""

result = str(intersection_set)
for i in result:
    if i.isnumeric(): print(i, end=' ')