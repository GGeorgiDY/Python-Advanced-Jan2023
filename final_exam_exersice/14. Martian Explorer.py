matrix = []

deposits_dict = {'water': 0, 'metal': 0, 'concrete': 0}

for row in range(6):
    matrix.append(input().split())
    if "E" in matrix[row]:
        rover_position = [row, matrix[row].index("E")]

# print(matrix)
# [['-', 'R', '-', '-', '-', '-'],
#  ['-', '-', '-', '-', '-', 'R'],
#  ['-', 'E', '-', 'R', '-', '-'],
#  ['-', 'W', '-', '-', '-', '-'],
#  ['-', '-', '-', 'C', '-', '-'],
#  ['M', '-', '-', '-', '-', '-']]
# print(rover_position)
# [2, 1]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

commands = input().split(', ')
# print(commands)
# ['down', 'right', 'down', 'right', 'down', 'left', 'left', 'left']

for command in commands:
    row = rover_position[0] + directions[command][0]
    col = rover_position[1] + directions[command][1]

    # if 0 > row:
    #     row = 5
    # elif row >= 6:
    #     row = 0
    # if 0 > col:
    #     col = 5
    # elif row >= 6:
    #     col = 0
    # не го пиша по-горния начин защото ми дава run time error

    if col > 5 or col < 0:
        col = 6 - abs(col)
    if row > 5 or row < 0:
        row = 6 - abs(row)

    if matrix[row][col] == "W":
        deposits_dict['water'] += 1
        rover_position = [row, col]
        print(f"Water deposit found at {(row, col)}")

    elif matrix[row][col] == "M":
        deposits_dict['metal'] += 1
        rover_position = [row, col]
        print(f"Metal deposit found at {(row, col)}")

    elif matrix[row][col] == "C":
        deposits_dict['concrete'] += 1
        rover_position = [row, col]
        print(f"Concrete deposit found at {(row, col)}")

    elif matrix[row][col] == "R":
        rover_position = [row, col]
        print(f"Rover got broken at {(row, col)}")
        break

    rover_position = [row, col]

if deposits_dict['water'] > 0 and deposits_dict['metal'] > 0 and deposits_dict['concrete'] > 0:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")

# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left

# R - - - - -
# - - C - - -
# - - - - M -
# - - W - - -
# - E - W - R
# - - - - - -
# up, right, down, right, right, right

# R - - - - -
# - - C - - -
# - - - - M -
# C - M - R M
# - E - W - -
# - - - - - -
# right, right, up, left, left, left, left, left



