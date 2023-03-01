lines = int(input())
elements_set = set()

for _ in range(lines):
    elements = input().split()
    for element in elements:
        elements_set.add(element)

for i in elements_set:
    print(i)