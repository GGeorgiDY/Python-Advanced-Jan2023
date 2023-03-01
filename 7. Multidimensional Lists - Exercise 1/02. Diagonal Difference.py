lines = int(input())
matrix = [input().split() for x in range(lines)]

first_diagonal, second_diagonal = [], []
for i in range(lines):
    first_diagonal.append(matrix[i][i])
    second_diagonal.append(matrix[i][lines - i - 1])

result = abs(sum(map(int, first_diagonal)) - sum(map(int, second_diagonal)))
print(result)

# принтирай разликата между сумите на двата диагонала в абсолютна ст-ст
# 3
# 11 2 4
# 4 5 6
# 10 8 -12


