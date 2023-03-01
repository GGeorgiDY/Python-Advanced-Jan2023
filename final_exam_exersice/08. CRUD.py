size = 6
matrix = [[x for x in input().split()] for x in range(size)]
position = [int(x) for x in input() if x.isdigit()]
# print(position) [1, 1]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(', ')
    if command[0] == 'Create':
        direction = command[1]
        value = command[2]
        r = int(position[0]) + int(directions[direction][0])
        c = int(position[1]) + int(directions[direction][1])

        if 0 <= r < size and 0 <= c < size:
            position = [r, c]
            if matrix[r][c] == '.':
                matrix[r][c] = value

    elif command[0] == 'Update':
        direction = command[1]
        value = command[2]
        r = int(position[0]) + int(directions[direction][0])
        c = int(position[1]) + int(directions[direction][1])

        if 0 <= r < size and 0 <= c < size:
            position = [r, c]
            if matrix[r][c] != '.':
                matrix[r][c] = value

    elif command[0] == 'Delete':
        direction = command[1]
        r = int(position[0]) + int(directions[direction][0])
        c = int(position[1]) + int(directions[direction][1])

        if 0 <= r < size and 0 <= c < size:
            position = [r, c]
            if matrix[r][c] != '.':
                matrix[r][c] = '.'

    elif command[0] == 'Read':
        direction = command[1]
        r = int(position[0]) + int(directions[direction][0])
        c = int(position[1]) + int(directions[direction][1])

        if 0 <= r < size and 0 <= c < size:
            position = [r, c]
            if matrix[r][c] != '.':
                print(matrix[r][c])

for row in matrix:
    print(' '.join(row))



# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop

# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
# (2, 3)
# Create, down, o
# Delete, right
# Read, up
# Create, left, 20
# Update, up, P
# Stop

# H 8 . . . .
# 70 i . . . .
# t . . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
# (0, 0)
# Read, right
# Read, down
# Read, left
# Delete, down
# Create, right, 10
# Read, left
# Stop



