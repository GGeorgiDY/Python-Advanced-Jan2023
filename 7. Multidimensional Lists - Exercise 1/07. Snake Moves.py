# тази задача е аналогична на змията която сме играли като малки
# змията като върви от ляво на дясно, след това отива на долния ред и продължава от дясно на ляво
# след като стигне най в ляво слиза на долния ред и продължава от ляво на дясно и т.н.
rows, cols = tuple(map(int, input().split()))
snake = input()
matrix = []
idx = 0

for row in range(rows):
    result = ''
    for col in range(cols):
        result += snake[idx % len(snake)]
        idx += 1

    if row % 2 == 0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])

for row in matrix:
    print(*row, sep='')

# 5 6
# SoftUni


# from collections import deque
#
# rows, cols = tuple(map(int, input().split()))
# word = deque(input())
# current_index = 0
# result = ''
# matrix = []
#
# for i in range(rows):
#     while True:
#         if current_index == cols:
#             if i % 2 == 0:
#                 matrix.append(result)
#             else:
#                 matrix.append(result[::-1])
#             result = ''
#             current_index = 0
#             break
#         result += word[0]
#         word.append(word.popleft())
#         current_index += 1
#
# print(*matrix, sep='\n')