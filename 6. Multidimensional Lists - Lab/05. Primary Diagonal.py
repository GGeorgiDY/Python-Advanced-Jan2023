lines = int(input())
matrix = []

for i in range(lines):
    matrix.append([int(x) for x in input().split()])
# print(matrix)
# [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

diagonal = 0
for idx in range(lines):
    diagonal += matrix[idx][idx]
print(diagonal)

# събери диагоналните стойности от матрицата
# 3
# 11 2 4
# 4 5 6
# 10 8 -12



