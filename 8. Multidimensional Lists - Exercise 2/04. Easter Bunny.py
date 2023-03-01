# имаме заек в матрица, който ще трябва да отиде на 4те страни и да събере яйцата, представляващи числа от индексите в
# матрицата. Ако срещне дупка или излезе от матрицата той трябва да спре. Трябва да принтираме по кой път е събрал най-
# много яйца, самия път описан стъпка по стъпка и коя е посоката

size = int(input())
matrix = []
bunny_pos = []
best_path = []
best_direction = None
max_collected_eggs = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    # намираме позицията на заека
    if "B" in line:
        bunny_pos = [row, line.index("B")]

# прочитаме всяка една от посоките които имаме възможно (те са ни в речника, който съм описал по-горе)
for direction, positions in directions.items():
    # трябва да запазим новата позиция, като я спираме с текущата
    # за целта първо определяме реда и колоната, по която ще вървим. Това не променя позицията на заека,
    # а само позицията, на която той би отишъл
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
        ]
    path = []
    collected_eggs = 0

    # казваме че докато се намираме в матрицата
    while 0 <= row < size and 0 <= col < size:
        # ако стигнем до капан прекратяваме цикъла
        if matrix[row][col] == "X":
            break

        # иначе събраните яйца трябва да бъдат увеличени със ст-та, която я има на определения индекс в матрицата
        collected_eggs += int(matrix[row][col])
        # след това трябва и да си добавим пътя
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    # сега трябва да проверим дали събраните яйца са повече или равни на максимално събраните яйца
    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*[i for i in best_path], sep='\n')
print(max_collected_eggs)

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
