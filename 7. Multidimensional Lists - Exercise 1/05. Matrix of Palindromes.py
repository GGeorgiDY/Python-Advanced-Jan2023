# трябва да направим матрица, която да съдържа палиндроми
rows, cols = tuple(map(int, input().split()))
matrix = []

for row in range(rows):
    lst = []
    for col in range(cols):
        current_string = chr(97 + row) + chr(97 + col + row) + chr(97 + row)
        lst.append(current_string)
    matrix.append(lst)

# print(matrix)
# [['aaa', 'aba', 'aca', 'ada', 'aea', 'afa'],
# ['bbb', 'bcb', 'bdb', 'beb', 'bfb', 'bgb'],
# ['ccc', 'cdc', 'cec', 'cfc', 'cgc', 'chc'],
# ['ddd', 'ded', 'dfd', 'dgd', 'dhd', 'did']]

for row in matrix:
    print(*row)

# 4 6
#
#
# 3 2
