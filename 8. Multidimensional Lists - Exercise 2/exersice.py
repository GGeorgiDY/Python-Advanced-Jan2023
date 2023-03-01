# n = int(input())
# matrix = [[x for x in input()] for x in range(n)]
# # print(matrix) [['0', 'K', '0', 'K', '0'], ['K', '0', '0', '0', 'K'], ['0', '0', 'K', '0', '0'], ['K', '0', '0', '0', 'K'], ['0', 'K', '0', 'K', '0']]
#
# removed_knights = 0
# directions = (
#     (-2, -1),
#     (-2, 1),
#     (2, -1),
#     (2, 1),
#     (-1, -2),
#     (-1, 2),
#     (1, 2),
#     (1, -2),
# )
#
# while True:
#     max_attacks = 0
#     knight_with_most_attacks = []
#     for row in range(n):
#         for col in range(n):
#             if matrix[row][col] == "K":
#                 current_attacks = 0
#                 for pos in directions:
#                     pos_row = row + pos[0]
#                     pos_col = col + pos[1]
#                     if 0 <= pos_row < n and 0 <= pos_col < n:
#                         if matrix[pos_row][pos_col] == "K":
#                             current_attacks += 1
#                 if current_attacks > max_attacks:
#                     max_attacks = current_attacks
#                     knight_with_most_attacks = [row, col]
#
#     if knight_with_most_attacks:
#         matrix[knight_with_most_attacks[0]][knight_with_most_attacks[1]] = "O"
#         removed_knights += 1
#     else:
#         break
#
# print(removed_knights)

# /////////////////////////////////////////////////////////////////////////////////////////////////

# n = int(input())
# matrix = []
# bunny_pos = []
# best_path = []
# max_collected_eggs = 0
# best_direction = None
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for row in range(n):
#     matrix.append(input().split())
#     if "B" in matrix[row]:
#         bunny_pos = [row, matrix[row].index("B")]
#
# for direction, positions in directions.items():
#     row, col = [
#         bunny_pos[0] + positions[0],
#         bunny_pos[1] + positions[1]
#     ]
#     collected_eggs = 0
#     path = []
#
#     while 0 <= row < n and 0 <= col < n:
#         if matrix[row][col] == "X":
#             break
#         collected_eggs += int(matrix[row][col])
#         path.append([row, col])
#
#         row += positions[0]
#         col += positions[1]
#
#     if collected_eggs > max_collected_eggs:
#         max_collected_eggs = collected_eggs
#         best_path = path
#         best_direction = direction
#
# print(best_direction)
# print(*best_path, sep='\n')
# print(max_collected_eggs)

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# /////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(input())
# matrix = []
# total_tea_bags = 0
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for row in range(size):
#     matrix.append(input().split())
#     if "A" in matrix[row]:
#         alice_pos = [row, matrix[row].index("A")]
# # print(alice_pos) [0, 1]
#
# while total_tea_bags < 10:
#     command = input()
#     row, col = directions[command]
#     matrix[alice_pos[0]][alice_pos[1]] = "*"
#     new_row, new_col = [
#         alice_pos[0] + row,
#         alice_pos[1] + col
#     ]
#     if 0 <= new_row < size and 0 <= new_col < size and matrix[new_row][new_col] == "R":
#         matrix[new_row][new_col] = "*"
#         print("Alice didn't make it to the tea party.")
#         for row in matrix:
#             print(' '.join(row))
#         raise SystemExit
#     alice_pos = [new_row, new_col]
#     if matrix[new_row][new_col].isnumeric():
#         total_tea_bags += int(matrix[alice_pos[0]][alice_pos[1]])
#     matrix[new_row][new_col] = "*"
#
#
# print("She did it! She went to the party.")
# for row in matrix:
#     print(' '.join(row))

# /////////////////////////////////////////////////////////////////////////////////////////////////

# matrix = []
# total_targets = 0
# targets = []
# shoot_targets = 0
# size = 5
# for row in range(size):
#     matrix.append(input().split())
#     if "A" in matrix[row]:
#         position = [row, matrix[row].index("A")]
#     if "x" in matrix[row]:
#         total_targets += matrix[row].count("x")
# # print(position) [2, 1]
# # print(total_targets) 4
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for _ in range(int(input())):
#     command = input().split()
#     if command[0] == "move":
#         direction = command[1]
#         steps = int(command[2])
#         marker = False
#         for i in range(int(steps)):
#             if not marker:
#                 row, col = directions[direction]
#                 hit_row = position[0] + row
#                 hit_col = position[1] + col
#
#                 if 0 <= hit_row < size and 0 <= hit_col < size:
#                     if matrix[hit_row][hit_col] == ".":
#                         position = [hit_row, hit_col]
#                     else:
#                         marker = True
#
#     elif command[0] == "shoot":
#         direction = command[1]
#         row, col = directions[direction]
#         hit_row = position[0] + row
#         hit_col = position[1] + col
#
#         while 0 <= hit_row < size and 0 <= hit_col < size:
#             if matrix[hit_row][hit_col] == "x":
#                 targets.append([hit_row, hit_col])
#                 shoot_targets += 1
#                 matrix[hit_row][hit_col] == "."
#                 break
#
#         hit_row += row
#         hit_col += col
#
# if total_targets <= shoot_targets:
#     print(f"Training completed! All {total_targets} targets hit.")
#     for target in targets:
#         print(target)
# else:
#     print(f"Training not completed! {total_targets - shoot_targets} targets left.")
#     for target in targets:
#         print(target)

# /////////////////////////////////////////////////////////////////////////////////////////////////

number_of_presents = int(input())
size = int(input())
total_nice_kids = 0
nice_kid = 0
matrix = []
for row in range(size):
    matrix.append(input().split())
    if "S" in matrix[row]:
        position = [row, matrix[row].index("S")]
    if "V" in matrix[row]:
        total_nice_kids += matrix[row].count("V")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

cookie_directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

command = input()
while number_of_presents > 0 and command != "Christmas morning":
    matrix[position[0]][position[1]] = "-"
    row = directions[command][0]
    col = directions[command][1]
    new_rol = position[0] + row
    new_col = position[1] + col

    if 0 <= new_rol < size and 0 <= new_col < size:
        position = [new_rol, new_col]
        if matrix[new_rol][new_col] == "X":
            matrix[new_rol][new_col] = "S"
        if matrix[new_rol][new_col] == "V":
            number_of_presents -= 1
            nice_kid += 1
            matrix[new_rol][new_col] = "S"

        if matrix[new_rol][new_col] == "C":
            matrix[new_rol][new_col] = "S"
            for direction in cookie_directions:
                row = direction[0]
                col = direction[1]
                if matrix[row][col] == "V":
                    number_of_presents -= 1
                    nice_kid += 1
                    matrix[row][col] = "-"
                elif matrix[row][col] == "X":
                    number_of_presents -= 1
                    matrix[row][col] = "-"
    command = input()

if number_of_presents <= 0 and total_nice_kids > nice_kid:
    print("Santa ran out of presents!")
for row in matrix:
    print(' '.join(row), sep="\n")
else:
    if total_nice_kids > nice_kid:
        print(f"No presents for {total_nice_kids - nice_kid} nice kid/s.")
    else:
        print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
