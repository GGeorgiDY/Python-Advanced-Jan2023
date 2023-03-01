from collections import deque

names = deque(input().split(', '))
size = 6
matrix = []
exit_direction = ()
pass_turn = [0, 0]

for row in range(size):
    matrix.append(input().split())

# print(matrix)
# [['.', '.', 'T', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.'],
# ['.', '.', 'W', '.', '.', '.'],
# ['.', '.', 'W', '.', '.', 'E'],
# ['.', '.', '.', '.', '.', '.'],
# ['.', 'T', '.', 'W', '.', '.']]

while True:
    command = input()
    row = int(command[1])
    col = int(command[4])

    if pass_turn[0] > 0:
        pass_turn[0] -= 1
        names.append(names.popleft())
        pass_turn[0], pass_turn[1] = pass_turn[1], pass_turn[0]
        continue

    if matrix[row][col] == "E":
        print(f"{names[0]} found the Exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{names[0]} is out of the game! The winner is {names[1]}.")
        break

    elif matrix[row][col] == "W":
        print(f"{names[0]} hits a wall and needs to rest.")
        pass_turn[0] = 1
        names.append(names.popleft())
        pass_turn[0], pass_turn[1] = pass_turn[1], pass_turn[0]
        continue

    names.append(names.popleft())
    pass_turn[0], pass_turn[1] = pass_turn[1], pass_turn[0]

# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)

# Jerry, Tom
# . T . . . W
# . . . . T .
# . W . . . T
# . T . E . .
# . . . . . T
# . . T . . .
# (1, 1)
# (3, 0)
# (3, 3)

# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)

