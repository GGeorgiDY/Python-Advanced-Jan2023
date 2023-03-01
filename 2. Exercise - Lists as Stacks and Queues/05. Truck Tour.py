from collections import deque

pumps = deque([[int(x) for x in input().split()] for _ in range (int(input()))]) # ([[1, 5], [10, 3], [3, 4]])

pumps_copy = pumps.copy()
index = 0
gas_in_tank = 0

while pumps_copy:
    petrol, distance = pumps_copy.popleft()
    gas_in_tank += petrol

    if gas_in_tank - distance <0:
        pumps.rotate(-1)
        index += 1
        gas_in_tank = 0
        pumps_copy = pumps.copy()
    else:
        gas_in_tank -= distance

print(index)


# 3
# 1 5
# 10 3
# 3 4
