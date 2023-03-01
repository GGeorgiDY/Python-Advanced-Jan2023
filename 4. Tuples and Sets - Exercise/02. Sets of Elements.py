lines = input().split()
first_line = int(lines[0])
second_line = int(lines[1])

n = set()
m = set()

for i in range(first_line):
    number = int(input())
    n.add(number)

for y in range(second_line):
    number = int(input())
    m.add(number)

intersection_set = set(n.intersection(m))
for i in intersection_set:
    print(i)