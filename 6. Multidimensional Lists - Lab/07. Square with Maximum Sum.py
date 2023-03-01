# намери най-голямата сума от 2х2 числата в матрицата и притнирай тази извадка
rows, cols = tuple(map(int, input().split(', ')))
matrix = [input().split(', ') for i in range(rows)]
maximum_sum = 0
biggest_matrix = []

for row in range(rows-1):
    for col in range(cols-1):
        square = [
            list(map(int, [matrix[row][col], matrix[row][col+1]])),
            list(map(int, [matrix[row+1][col], matrix[row+1][col+1]]))
            ]
        if sum(sum(square, [])) > maximum_sum:
            maximum_sum = sum(sum(square, []))
            biggest_matrix = square

for row in biggest_matrix:
    print(*row)
print(maximum_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, utils
