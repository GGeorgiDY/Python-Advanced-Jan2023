# matrix = []
# for i in range(3):
# 	matrix.append([])
# 	for j in range(2):
# 		matrix[i].append(0)
# print(matrix)

##################################################################################################

# rows, cols = [int(x) for x in input().split(', ')]
# matrix = []
# for row in range(rows):
# 	matrix.append([int(x) for x in input().split()])
# # print(matrix) [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
#
# for col in range(cols):
# 	result = 0
# 	for row in range(rows):
# 		result += matrix[row][col]
# 	print(result)

##################################################################################################

# lines = int(input())
# matrix = []
#
# for i in range(lines):
# 	matrix.append([int(x) for x in input().split()])
#
# diagonal = 0
# for row in range(len(matrix)):
# 	for col in range(len(matrix)):
# 		if row == col:
# 			diagonal += matrix[row][col]
# print(diagonal)
#
# opposite_diagonal = 0
# # counter = 0
# # for row in range(len(matrix) -1, -1, -1): #от 2 до 0 включително
# # 	opposite_diagonal += matrix[row][counter]
# # 	counter += 1
# for row in range(len(matrix) -1, -1, -1): #от 2 до 0 включително
# 	opposite_diagonal += matrix[row][(len(matrix) - 1) - row]
# print(opposite_diagonal)
#
# sum_of_left_half = 0
# for row in range(len(matrix)):
# 	for col in range(row +1):
# 		sum_of_left_half += matrix[row][col]
# print(sum_of_left_half)
#
# sum_of_left_half_exclusive = 0
# for row in range(len(matrix)):
# 	for col in range(row):
# 		sum_of_left_half_exclusive += matrix[row][col]
# print(sum_of_left_half_exclusive)
#
# sum_of_right_half = 0
# for row in range(len(matrix)):
# 	for col in range(row, len(matrix)):
# 		sum_of_right_half += matrix[row][col]
# print(sum_of_right_half)
#
# sum_of_right_half_exclusive = 0
# for row in range(len(matrix)):
# 	for col in range(row + 1, len(matrix)):
# 		sum_of_right_half_exclusive += matrix[row][col]
# print(sum_of_right_half_exclusive)

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

##################################################################################################

# lines= int(input())
# matrix = []
# for i in range(lines):
# 	line = input()
# 	matrix.append([x for x in line])
# # print(matrix) [['A', 'B', 'C'], ['D', 'E', 'F'], ['X', '!', '@']]
#
# searched_el = input()
# # for row in range(len(matrix)):
# # 	cols = len(matrix[row])
# # 	for col in range(cols):
# # 		if searched_el == matrix[row][col]:
# # 			print(f"{(row, col)}")
#
# flag = False
# for row in range(len(matrix)):
# 	cols = len(matrix[row])
# 	for col in range(cols):
# 		if searched_el == matrix[row][col]:
# 			print(f"{(row, col)}")
# 			flag = True
# 			break
# 	if flag:
# 		break
#
# if not flag:
# 	print(f"{searched_el} does not occur in the matrix")

# 4
# asdd
# xczc
# qwee
# qefw
# 4

# 3
# ABC
# DEF
# X!@
# !

##################################################################################################

rows, cols = [int(x) for x in input().split(', ')]
matrix = []
biggest_matrix = []
biggest_sum = 0
for row in range(rows):
	matrix.append([int(x) for x in input().split(', ')])
# print(matrix) [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

for row in range(rows -1):
	for col in range(cols -1):
		square = [
			[matrix[row][col], matrix[row][col + 1]],
			[matrix[row + 1][col], matrix[row + 1][col + 1]]
		]
		result = [x for el in square for x in el]
		current_sum = sum(result)
		if current_sum > biggest_sum:
			biggest_sum = current_sum
			biggest_matrix = square

for row in biggest_matrix:
	print(*row)
print(biggest_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
