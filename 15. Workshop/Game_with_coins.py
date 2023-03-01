player_one_symbol = "1"
player_two_symbol = "2"

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
)
turn = [[1, player_one_symbol], [2, player_two_symbol]]  # turn.append(turn.pop(0)

rows, cols = 6, 7
board = [['0'] * cols for row in range(rows)]
# print(*board, sep="\n")
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']

while True:
    [print(f"[ {', '.join(row)} ]") for row in board]
    player_number, player_symbol = turn[0]
    player_col = int(input(f"\nPlayer{player_number}, please choose a column: ")) - 1

    # проверяваме дали подадената колона е в правилния range
    if not 0 <= player_col < cols:
        print(f"Select a valid number in the range ({1}{cols})")
        continue

    # проверяваме дали колоната не е запълнена до горе със символи (дали е заета)
    row = 0
    if board[row][player_col] != "0":
        print("No empty spaces on that row!")
        continue

    # проверяваме ако реда е последния в матрицата или ако на следващия ред има нещо различко от "0", да сложим на този
    # ред символа на играча. Ако не, увеличи реда с +1 за да намерим къде да сложим символа на играча.
    while True:
        if row == rows - 1 or board[row + 1][player_col] != "0":
            board[row][player_col] = player_symbol
            break
        row += 1

    # обхождаме всяко поле в матрицата и ако това поле кореспондира на символа на играча от текущия ход
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player_symbol:
                continue

            # проверяваме всяка възможна дирекция. Създаваме си две променливи "r" и "c" които да са ни равни на
            # текущия ред и колона (тази в която сме намерили символ на играча от този ход)
            for coordinates in directions:
                r, c = row, col

                # тези 2 променливи ги променяме на база дирекцията ни, 4 пъти
                for _ in range(3):
                    r, c = r + coordinates[0], c + coordinates[1]

                    # проверяваме дали излизаме от матрицата
                    if not (0 <= r < rows and 0 <= c < cols):
                        break

                    # проверяваме дали за всяка промяна в променливата, имаме от правилния символ
                    if board[r][c] != player_symbol:
                        break
                else:
                    [print(f"[ {', '.join(row)} ]") for row in board]
                    print(f"The winner is player: {player_number}")
                    raise SystemExit  # приключва цялта програма

    # променяме хода на играча
    turn.append(turn.pop(0))
