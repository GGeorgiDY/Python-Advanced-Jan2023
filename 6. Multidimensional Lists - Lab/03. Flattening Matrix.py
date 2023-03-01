# lines = int(input())
# lst = []
#
# for i in range(lines):
#     line = [int(x) for x in input().split(', ')]
#     lst.extend(line)
#
# print(lst)

number_of_rows = int(input())
matrix = []
for i in range(number_of_rows):
    matrix.append([int(x) for x in input().split(', ')])
# print(matrix)   [[10, 2, 21, 4], [5, 20, 41, 9], [6, 2, 4, 99]]

result = [x for el in matrix for x in el]
# print(result) [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]

print(result)




# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
