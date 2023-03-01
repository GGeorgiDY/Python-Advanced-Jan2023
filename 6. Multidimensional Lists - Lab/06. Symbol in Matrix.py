lines = int(input())
matrix = []

for _ in range(lines):
    matrix.append([x for x in input()])

# print(matrix)
# [['A', 'B', 'C'], ['D', 'E', 'F'], ['X', '!', '@']]

flag = False
target_char = input()
for row in range(lines):
    for col in range(lines):
        if target_char == matrix[row][col]:
            print(f"({row}, {col})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{target_char} does not occur in the matrix")

# идеята на кода е да провери дали последния символ го има в матрицата по-горе и ако да, да покаже на кои индекси го има
# 3
# ABC
# DEF
# X!@
# !

# 4
# asdd
# xczc
# qwee
# qefw
# 4
