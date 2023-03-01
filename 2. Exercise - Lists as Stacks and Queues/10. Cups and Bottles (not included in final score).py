from collections import deque

cups_capacity = deque(map(int, input().split()))
bottles_capacity = list(map(int, input().split()))
total_wasted_water = 0

while cups_capacity and bottles_capacity:
    current_bottle = bottles_capacity.pop()

    if cups_capacity[0] <= current_bottle:
        wasted_water = current_bottle - cups_capacity[0]
        total_wasted_water += wasted_water
        cups_capacity.popleft()
    else:
        cups_capacity[0] -= current_bottle

if not cups_capacity:
    print(f"Bottles: {' '.join(list(map(str, bottles_capacity)))}")
if not bottles_capacity:
    print(f"Cups: {' '.join(list(map(str, cups_capacity)))}")
print(f"Wasted litters of water: {total_wasted_water}")

# 4 2 10 5
# 3 15 15 11 6

# 1 5 28 1 4
# 3 18 1 9 30 4 5

# 10 20 30 40 50
# 20 11

