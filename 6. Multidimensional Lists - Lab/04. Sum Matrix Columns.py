rows, columns = [int(x) for x in input().split(', ')]
matrix = []

# тук ще направим обратното -> вместо да обходим първо по ред и след това по колона,
# ще обходим първо по колона и след това по ред
# за целта първо ще създадем матрицата, която след като е създадена ще я обходим по колона и ред
for row in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

# print(matrix)
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

for col in range(columns):
    result = 0
    for row in range(rows):
        result += matrix[row][col]
    print(result)

# трябва да сумираме всички редове в всяка една отделна колона
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
