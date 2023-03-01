# lines = int(input())
# names = []
# for i in range(lines):
#     names.append(input())

# unique_names = set(name for name in names)
# for name in unique_names:
#     print(name)
# може и като горния вариант

lines = int(input())
names = set()
for i in range(lines):
    names.add(input())

for name in names:
    print(name)


# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
