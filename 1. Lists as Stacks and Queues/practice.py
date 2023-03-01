from collections import deque

d = deque()
for i in range(5):
    d.append(i)

print(d)
print(d.popleft())
print(d)
