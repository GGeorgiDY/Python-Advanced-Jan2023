def eat_cockie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighbourhood[r][c].isalpha(): #ако е буква е True
            if neighbourhood[r][c] == 'V':
                nice_kids += 1

            neighbourhood[r][c] = '-'
            presents_left -= 1
        if not presents_left:
            break
    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighbourhood = []
santa_pos = []
total_nice_kids = 0
visited_nice_kids = 0

# тук си създаваме посоките в които ще ходи дядо коледа
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = input().split()
    neighbourhood.append(line) # изграждаме матрицата си
    if 'S' in line:
        santa_pos = [row, line.index('S')] # намираме коя е позицията на дядо коледа
        neighbourhood[row][santa_pos[1]] = '-' # махаме S от текущата позиция на дядо коледа
    total_nice_kids += line.count('V') # намираме броя на добрите деца във всеки ред и ги сумираме

command = input()

while True:
    if command == "Christmas morning":
        break

    # следващите 3 реда са объркващи, но реално променят текущата позиция на Дядо коледа, на база подадената команда,
    # чрез която се взима точната дирекция в речника. За това имаме +
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]
    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        visited_nice_kids += 1
        presents -= 1

    elif house == 'C':
        presents, visited_nice_kids = eat_cockie(presents, visited_nice_kids)

    neighbourhood[santa_pos[0]][santa_pos[1]] = '-'

    if not presents or visited_nice_kids == total_nice_kids:
        break
    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and visited_nice_kids < total_nice_kids:
    print("Santa ran out of presents!")

print(*[' '.join(row) for row in neighbourhood], sep="\n")

if visited_nice_kids == total_nice_kids:
    print(f"Good job, Santa! {visited_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - visited_nice_kids} nice kid/s.")
