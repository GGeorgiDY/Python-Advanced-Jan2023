n = int(input())
stack = []

for i in range(n):
    command = input()

    if command[0] == '1':
        stack.append(int(command.split()[1]))

    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()

    elif command[0] == '3':
        if len(stack) > 0:
            print(max(stack))

    elif command[0] == '4':
        if len(stack) > 0:
            print(min(stack))

for i in range(len(stack)):
    if len(stack) > 1:
        print(str(stack.pop()) + ', ', end="")
    else:
        print(str(stack.pop()))

# print(*stack[::-1], sep=', ')
# може и така да се напише вместо цикъла и иф-овете

# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
