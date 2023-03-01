# from collections import deque
#
# quantity_of_food = int(input())
# quantity_of_food_in_each_order = deque(map(int, input().split(' '))) #с map и int правим целата опашка да са int
# print(max(quantity_of_food_in_each_order))
#
# for _ in range(len(quantity_of_food_in_each_order)):
#     if len(quantity_of_food_in_each_order) > 0:
#         if int(quantity_of_food_in_each_order[0]) <= quantity_of_food:
#             quantity_of_food -= int(quantity_of_food_in_each_order.popleft())
#         else:
#             print(f"Orders left: {' '.join(map(str, quantity_of_food_in_each_order))}")
#             break
#
# if len(quantity_of_food_in_each_order) == 0:
#     print('Orders complete')

# 348
# 20 54 30 16 7 9

# 499
# 57 45 62 70 33 90 88 76 100 50


from collections import deque

quantity_of_food = int(input())
quantity_of_food_in_each_order = deque(map(int, input().split()))
print(max(quantity_of_food_in_each_order))

for i in range(len(quantity_of_food_in_each_order)):
    if len(quantity_of_food_in_each_order) > 0:
        if quantity_of_food >= quantity_of_food_in_each_order[0]:
            quantity_of_food -= quantity_of_food_in_each_order[0]
            quantity_of_food_in_each_order.popleft()
        else:
            break

if len(quantity_of_food_in_each_order) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(deque(map(str, quantity_of_food_in_each_order)))}")
