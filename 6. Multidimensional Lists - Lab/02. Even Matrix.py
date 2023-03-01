lines = int(input())
matrix = []

for i in range(lines):
    lst = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(lst)
print(matrix)


# 4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67


