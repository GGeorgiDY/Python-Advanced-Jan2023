n = int(input())
moves = input().split()
# print(move) ['up', 'right', 'right', 'up', 'right']

matrix = []
collected_coal = 0
total_coal = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    matrix.append(input().split())
    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index('s')]
        matrix[row][miner_pos[1]] = "*"
    total_coal += matrix[row].count("c")

for move in moves:
    r = miner_pos[0] + directions[move][0]
    c = miner_pos[1] + directions[move][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_pos = [r, c]
    if matrix[r][c] == "c":
        collected_coal += 1
        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")


# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *


