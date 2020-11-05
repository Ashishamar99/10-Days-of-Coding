import itertools

arr = []
for _ in range(int(input('Enter number of elements: '))):
    arr.append(int(input(f'Enter {_}th element: ')))

all_triplets = list(itertools.combinations(arr, 3))
results = []
for triplet in all_triplets:
    if sum(triplet) == 0:
        results.append(triplet)

for triplet in results: 
    for num in triplet: print(num, end=' ')
    print('\n')