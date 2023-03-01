size = int(input())
racing_number = input()
kilometers = 0
position = (0, 0)
tunnels = []
matrix = [[x for x in input().split()] for _ in range(size)]
# print(matrix) [['.', '.', '.', '.', '.'], ['.', '.', '.', 'T', '.'], ['.', '.', '.', '.', '.'], ['.', 'T', '.', '.', '.'], ['.', '.', 'F', '.', '.']]
for rows in range(size):
    for cols in range(size):
        if matrix[rows][cols] == "T":
            tunnels.append([rows, cols])
# print(tunnels) [[1, 3], [3, 1]]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if command == 'End':
        matrix[row][col] = "C"
        break

    r, c = directions[command]
    row = position[0] + r
    col = position[1] + c

    if 0 <= row <= size and 0 <= col <= size:
        position = (row, col)

        if matrix[row][col] == "T":
            kilometers += 30
            matrix[row][col] = "."
            tunnels.remove([row, col])
            # print(tunnels) [[3, 1]]
            position = (tunnels[0][0], tunnels[0][1])
            # print(position) (3, 1)
            matrix[position[0]][position[1]] = "."

        elif matrix[row][col] == ".":
            kilometers += 10

        elif matrix[row][col] == "F":
            kilometers += 10
            matrix[row][col] = "C"
            print(f"Racing car {racing_number} finished the stage!")
            print(f"Distance covered {kilometers} km.")
            for i in matrix:
                print(''.join(i))
            raise SystemExit

print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {kilometers} km.")
for i in matrix:
    print(''.join(i))

# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# down
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End

# 10
# 45
# . . . . . . . . . .
# . . T . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . F . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . T . .
# right
# down
# down
# right
# up
# left
# up
# up
# End

