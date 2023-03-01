# numbers = input().split(" ")
# reversed_numbers = []
# for i in range(len(numbers), 0, -1):
#     if len(numbers) > 0:
#         number = numbers[i-1]
#         reversed_numbers.append(number)
#
# print(' '.join(reversed_numbers))
# може да се реши и като горе

numbers = input().split(" ")
for _ in range(len(numbers)):
    print(numbers.pop() + ' ', end='')

# 1 2 3 4 5