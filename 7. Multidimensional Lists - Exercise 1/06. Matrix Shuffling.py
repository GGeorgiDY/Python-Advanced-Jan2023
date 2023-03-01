#създаваме си матрица, която след това обработваме, като разменяме стойностите на определени индекси
rows, cols = tuple(map(int, input().split()))
matrix = [input().split() for x in range(rows)]
# print(matrix)
# [['1', '2', '3'], ['4', '5', '6']]

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    elif int(command[1]) > rows or int(command[2]) > cols or int(command[3]) > rows or int(command[4]) > cols:
        print("Invalid input!")
    else:
        row_1 = int(command[1])
        col_1 = int(command[2])
        row_2 = int(command[3])
        col_2 = int(command[4])

        p1 = matrix[row_1][col_1]
        p2 = matrix[row_2][col_2]
        matrix[row_1][col_1] = p2
        matrix[row_2][col_2] = p1

        for row in matrix:
            print(*row)

# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END

# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END

