size = int(input())
submarine_life = 2
battlefield_cruisers = 0
matrix = []
for row in range(size):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        pos = [row, matrix[row].index("S")]
    if "C" in matrix[row]:
        battlefield_cruisers += matrix[row].count("C")
# print(matrix) [['*', '-', '-', '*', '-'], ['-', 'S', '-', '*', 'C'], ['-', '*', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', 'C', '-', '*', 'C']]
# print(pos) [1, 1]
# print(battlefield_cruisers) 3
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while submarine_life >= 0 and battlefield_cruisers != 0:
    command = input()
    row, col = directions[command]
    new_row = int(pos[0]) + int(row)
    new_col = int(pos[1]) + int(col)
    if 0 <= new_row < size and 0 <= new_col < size:
        matrix[pos[0]][pos[1]] = "-"
        pos = [new_row, new_col]
        if matrix[pos[0]][pos[1]] == "-":
            matrix[pos[0]][pos[1]] = "S"
        elif matrix[pos[0]][pos[1]] == "C":
            matrix[pos[0]][pos[1]] = "S"
            battlefield_cruisers -= 1
        elif matrix[pos[0]][pos[1]] == "*":
            submarine_life -= 1
            matrix[pos[0]][pos[1]] = "S"


if battlefield_cruisers == 0:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    for row in matrix:
        print(''.join(row), sep="\n")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {pos}!")
    for row in matrix:
        print(''.join(row), sep="\n")