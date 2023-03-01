# rows, columns = map(int, input().split(', '))# може и така
rows, columns = [int(x) for x in input().split(', ')]

matrix = []
counter = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows):
    for col in range(columns):
        counter += matrix[row][col]

print(counter)
print(matrix)


# class Matrix:
# 	def __init__(self):
# 		self.rows, self.cols = [int(x) for x in input().split(', ')]
# 		self.current_matrix = []
# 		for x in range(self.rows):
# 			self.current_matrix.append([int(x) for x in input().split(', ')])
#
# 	def read_matrix_func(self):
# 		return self.current_matrix
#
# 	def matrix_counter(self):
# 		current_counter = 0
# 		for row in range(self.rows):
# 			for col in range(self.cols):
# 				current_counter += self.current_matrix[row][col]
# 		return current_counter
#
#
#
# matrix = Matrix()
# print(matrix.matrix_counter())
# print(matrix.read_matrix_func())