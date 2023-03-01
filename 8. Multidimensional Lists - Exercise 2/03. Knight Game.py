# имаме шахматна дъска с коне на нея. Идеята е да направим така, че с най-малко движения да направим така че
# да някак как конете да се атакуват един друг
# това се прави като се маха коня който атакува най-много други коне

size = int(input())
matrix = [list(input()) for i in range(size)]
# [['0', 'K', '0', 'K', '0'], ['K', '0', '0', '0', 'K'], ['0', '0', 'K', '0', '0'], ['K', '0', '0', '0', 'K'], ['0', 'K', '0', 'K', '0']]

# правим си тюпъл с възможните позиции
positions = (
    (-2, 1),
    (-2, -1),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (1, 2),
    (-1, 2),
)

removed_knights = 0

# проверяваме кой е коня който атакува най-много други коне
while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks_pos = [row, col]

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)


# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
