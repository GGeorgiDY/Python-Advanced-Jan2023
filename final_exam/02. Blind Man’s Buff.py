n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(input().split())
    if "B" in matrix[i]:
        pos = [i, matrix[i].index("B")]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
moves_counter = 0
touched_opponents = 0

while True:
    command = input()
    if command == "Finish" or touched_opponents == 3:
        break

    row = pos[0] + directions[command][0]
    col = pos[1] + directions[command][1]
    if 0 <= row < n and 0 <= col < m:
        if matrix[row][col] == "P":
            touched_opponents += 1
            moves_counter += 1
            pos = [row, col]
        elif matrix[row][col] == "O":
            continue
        else:
            pos = [row, col]
            moves_counter += 1


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_counter}")
