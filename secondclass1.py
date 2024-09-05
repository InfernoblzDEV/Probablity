set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

union = set1.union(set2)

total_g = list(union)

print('The number of invited guest is: ', len(total_g))
print('The invited guests are: ', total_g)
