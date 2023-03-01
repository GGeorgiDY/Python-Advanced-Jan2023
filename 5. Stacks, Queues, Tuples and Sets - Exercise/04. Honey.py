# from collections import deque
#
# working_bees = deque(map(int, input().split()))
# nectar = list(map(int, input().split()))
# given_symbols = deque(input().split())
#
# total_honey_made = 0
#
# while nectar and working_bees:
#     if len(nectar) > 0 and len(working_bees) > 0 and working_bees[0] <= nectar[-1]:
#         if given_symbols[0] == "+":
#             total_honey_made += abs(working_bees[0] + nectar[-1])
#             working_bees.popleft()
#             nectar.pop()
#             given_symbols.popleft()
#
#         elif given_symbols[0] == "-":
#             total_honey_made += abs(working_bees[0] - nectar[-1])
#             working_bees.popleft()
#             nectar.pop()
#             given_symbols.popleft()
#
#         elif given_symbols[0] == "*":
#             total_honey_made += abs(working_bees[0] * nectar[-1])
#             working_bees.popleft()
#             nectar.pop()
#             given_symbols.popleft()
#
#         else:
#             if nectar == 0 or working_bees == 0:
#                 continue
#             total_honey_made += abs(working_bees[0] / nectar[-1])
#             working_bees.popleft()
#             nectar.pop()
#             given_symbols.popleft()
#
#     else:
#         nectar.pop()
#
# print(f"Total honey made: {total_honey_made}")
# if working_bees:
#     print(f"Bees left: {', '.join(map(str, working_bees))}")
# if nectar:
#     print(f"Nectar left: {', '.join(map(str, nectar))}")



from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
total_honey = 0

operations = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
}

while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    elif curr_nectar > curr_bee:
        total_honey += abs(operations[symbols.popleft()](curr_bee, curr_nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")



# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
