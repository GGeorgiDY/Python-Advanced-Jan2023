# from builtins import function
#
# first_set = set(input().split())
# second_set = set(input().split())
# # print(first_set, second_set) {'1', '4', '3', '2', '5'} {'1', '3', '2'}
#
# n = int(input())
# for _ in range(n):
#     command = input()
#     if "Add First" in command:
#         # numbers = command.split()[2:] вместо следващия ред, може и така да вземем само числата
#         command = command.replace("Add First ", "")
#         first_set = first_set.union(command.split())
#
#     elif "Add Second" in command:
#         command = command.replace("Add Second ", "")
#         second_set = second_set.union(command.split())
#
#     elif "Remove First" in command:
#         command = command.replace("Remove First ", "")
#         for number in command.split():
#             if number in first_set:
#                 first_set.remove(number)
#
#     elif "Remove Second" in command:
#         command = command.replace("Remove Second ", "")
#         for number in command.split():
#             if number in second_set:
#                 second_set.remove(number)
#
#     elif "Check Subset" in command:
#         if first_set.issubset(second_set) or second_set.issubset(first_set):
#             print("True")
#         else:
#             print("False")
#
#
# print(', '.join(map(str, sorted(map(int, first_set)))))
# print(', '.join(map(str, sorted(map(int, second_set)))))
# не ги сортираше правилно защото бяха стрингове. За това ги направих числа, които за да ги join-a трябваше
# пак да ги направя накравя стрингове

# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset

# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5


# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
#
# n = int(input())
# for _ in range(n):
#     first_command, *data = input().split()
#     command = first_command + ' ' + data.pop(0)
#
#     if data == "Add First":
#         [first_set.add(int(x)) for x in data]
#
#     elif data == "Add Second":
#         [second_set.add(int(x)) for x in data]
#
#     elif data == "Remove First":
#         [first_set.discard(int(x)) for x in data]
#
#     elif data == "Remove Second":
#         [second_set.discard(int(x)) for x in data]
#
#     else:
#         if first_set.issubset(second_set) or second_set.issubset(first_set):
#             print(True)
#         else:
#             print(False)
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")


first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_set.add(el) for el in x],
    "Add Second": lambda x: [second_set.add(el) for el in x],
    "Remove First": lambda x: [first_set.discard(el) for el in x],
    "Remove Second": lambda x: [second_set.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first_set.issubset(second_set) or second_set.issubset(first_set) else print(False)
             }

n = int(input())
for _ in range(n):
    first_command, *data = input().split()
    command = first_command + ' ' + data.pop(0)

    if data:
        functions[command]([int(x) for x in data])
    else:
        functions[command]()

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")