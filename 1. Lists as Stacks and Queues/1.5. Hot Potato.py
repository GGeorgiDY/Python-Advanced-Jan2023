from collections import deque

kids = deque(input().split())
n = int(input())
counter = 1

while len(kids) > 1:
    kid = kids.popleft()
    if counter == n:
        print(f'Removed {kid}')
        counter = 1
    else:
        kids.append(kid)
        counter += 1

winner = kids.popleft()
print(f'Last is {winner}')

