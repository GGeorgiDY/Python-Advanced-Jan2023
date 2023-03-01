lines = int(input())

matrix = [input().split(', ') for x in range(lines)]
# print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

primary_diagonal, secondary_diagonal = [], []

for idx in range(lines):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][lines - idx - 1])
print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(map(int, primary_diagonal))}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(map(int, secondary_diagonal))}")


# тук идеята е да извадим двата диагонала и тяхната индивидуална сума
#
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
