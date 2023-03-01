size = int(input())
matrix = [list(map(int, input().split())) for x in range(size)]

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    action = command[0]

    if action == "Add":
        row_idx = int(command[1])
        col_idx = int(command[2])
        if 0 <= row_idx < size and 0 <= col_idx < size:
            matrix[row_idx][col_idx] += int(command[3])
        else:
            print("Invalid coordinates")

    elif action == "Subtract":
        row_idx = int(command[1])
        col_idx = int(command[2])
        if 0 <= row_idx < size and 0 <= col_idx < size:
            matrix[row_idx][col_idx] -= int(command[3])
        else:
            print("Invalid coordinates")

for row in matrix:
    print(*row)

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
