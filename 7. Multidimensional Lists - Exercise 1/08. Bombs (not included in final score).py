n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
# print(matrix) [[8, 3, 2, 5], [6, 4, 7, 9], [9, 9, 3, 6], [6, 8, 1, 2]]
coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, -1),#up-left
    (-1, 0), #up
    (-1, 1), #up-right
    (0, -1), #left
    (0, 1), #right
    (1, 0), #down
    (1, -1), #down-left
    (1, 1), #down-right
    (0, 0) #current position
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y
        # проверяваме дали координатите са валидни
        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = 0
sum_of_alived_cells = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_of_alived_cells += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alived_cells}")
[print(*matrix[r]) for r in range(n)]