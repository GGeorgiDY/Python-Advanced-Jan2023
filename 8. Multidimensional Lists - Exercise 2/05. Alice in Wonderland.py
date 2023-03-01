size = int(input())
matrix = []
alice_pos = []
tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if 'A' in line:
        alice_pos = [row, line.index('A')]
        matrix[row][alice_pos[1]] = '*'

while tea_bags < 10:
    direction = input()
    row = 0
    col = 0
    row += alice_pos[0] + directions[direction][0]
    col += alice_pos[1] + directions[direction][1]

    # проверяваме дали Алиса ще излезе от матрицата
    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    # проверяваме дали Алиса не е попаднала в заешката дупка
    if position == 'R':
        break
    elif position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn\'t make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in matrix], sep="\n")

# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right

