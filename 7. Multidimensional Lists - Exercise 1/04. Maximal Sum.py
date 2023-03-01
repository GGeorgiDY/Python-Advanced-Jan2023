# трябва да намерим в матрицата къде 3х3 сумата от елементите е най-голяма
rows, cols = tuple(map(int, input().split()))
matrix = [input().split() for x in range(rows)]
max_sum = - 999999
biggest_square = []

for row in range(rows -2):# това го правим за да не излезем out of range при редовете
    for col in range(cols -2):# това го правим за да не излезем out of range при колоните
        square =[
        list(map(int, [matrix[row][col], matrix[row][col+1], matrix[row][col+2]])), #тук ги преобразуваме в int
        list(map(int, [matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]])),#тук ги преобразуваме в int
        list(map(int, [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]])) #тук ги преобразуваме в int
        ]
        if sum(sum(square, [])) > max_sum: # така сумираме матрици
            biggest_square = square
            max_sum = sum(sum(square, []))

print(f"Sum = {sum(sum(biggest_square, []))}")
for row in biggest_square:
    print(' '.join(map(str, row)))

# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5

# rows, cols = [int(x) for x in input().split()]
# matrix = []
# maximum_sum = -999999
# biggest_matrix = []
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split()])
# # print(matrix) [[1, 5, 5, 2, 4], [2, 1, 4, 14, 3], [3, 7, 11, 2, 8], [4, 8, 12, 16, 4]]
#
# for row in range(rows -2):
#     for col in range(cols -2):
#         first_row = matrix[row][col:col + 3]
#         second_row = matrix[row + 1][col:col + 3]
#         third_row = matrix[row + 2][col:col + 3]
#         current_sum = sum(first_row) + sum(second_row) + sum(third_row)
#         if current_sum > maximum_sum:
#             maximum_sum = current_sum
#             biggest_matrix = [first_row, second_row, third_row]
# print(f"Sum = {maximum_sum}")
# [print(*biggest_matrix[row]) for row in range(3)]