# трябва да намерим колко еднакви 2х2 (два поредни) индексва в матриците имаме
rows, cols = tuple(map(int, input().split())) # print(rows, cols)   => 3 4
matrix = [input().split() for x in range(rows)] # [['A', 'B', 'B', 'D'], ['E', 'B', 'B', 'B'], ['I', 'J', 'B', 'B']]
# print(len(matrix)) => 3 брои броя на редовете

counter = 0
for row in range(len(matrix) -1): #взема 3те листа (редовете) като индекси без последния индекс => 0,1
    for col in range(len(matrix[row]) -1): #взема колоните като индекси без последния индекс => 0,1,2
        if col < cols and row < rows:# вместо да пишем горе -1, можеше да напишем тази проверка (сега -1 съм го оставил
            #защото не пречи на решението на задачата)
            if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
                counter += 1

print(counter)

# 3 4
# A B B D
# E B B B
# I J B B
