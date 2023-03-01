from collections import deque

chocolate_line = list(map(int, input().split(", ")))# ['20', '24', '-5', 'utils', '22', '60', '26']
milk_cups = deque(map(int, input().split(", ")))# deque([26, 60, 22, utils, 24, 10, 55])
milkshakes = 0

while milkshakes < 5 and chocolate_line and milk_cups:

    flag = False
    if chocolate_line[-1] <= 0:
        chocolate_line.pop()
        flag = True

    if milk_cups[0] <= 0:
        milk_cups.popleft()
        flag = True

    if flag:
        continue

    if chocolate_line[-1] == milk_cups[0]:
        milkshakes += 1
        chocolate_line.pop()
        milk_cups.popleft()
    else:
        milk_cups.append(milk_cups.popleft())
        chocolate_line[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_line:
    print(f"Chocolate: {', '.join(map(str, chocolate_line))}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(map(str, milk_cups))}")
else:
    print("Milk: empty")


# 20, 24, -5, utils, 22, 60, 26
# 26, 60, 22, utils, 24, 10, 55

# -10, -2, -30, 10
# -5

# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
