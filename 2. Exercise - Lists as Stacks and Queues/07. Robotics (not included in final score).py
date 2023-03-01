from collections import deque
from datetime import datetime, timedelta

lst = list(x for x in input().split(";")) #['ROB-15', 'SS2-10', 'NX8000-3']
robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in lst} #{'ROB': [15, 0], 'SS2': [10, 0], 'NX8000': [3, 0]}
# пазим речник с името на робота, времето за изпълнение на задача, времето за текущата задача

# горния компрехеншън може да се напише така
# robots = {}
# for r in input().split(";"):
#     name, time_needed = r.split("-")
#     robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)
# print(products)     deque(['detail', 'glass', 'wood', 'apple'])

while products:
    factory_time += timedelta(0, 1) #увеличаваме времето с 1 сек
    product = products.popleft()

    # намаляме времето на робота, ако той е зает с нещо
    robots = {r[0]: [r[1][0], r[1][1] -1] if r[1][1] !=0 else r[1] for r in robots.items()}

    # горния компрехеншън може да се напише така
    # for name, value in robots.items():
    #     if value[1] != 0:
    #         robots[name][1] -= 1


    # взимаме всички свободни роботи
    # filter итерира през някаква колекция. В този случай той прави for цикъл for x in robots.items() и връща ще
    # върне само онези стойности, които изпълняват условието x[1][1] == 0
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    # горния код може да се напише така
    # free_robots = []
    # for name, value in robots.items():
    #     if value[1] != 0:
    #         robots[name][1] -= 1
    # for name, value in robots.items():
    #     if value[1] == 0:
    #         free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robots[free_robots[0][0]] [1] = free_robots[0][1][0]

    # горния код може да се напише така
    # robot_name, data = free_robots[0]
    # robots[robot_name][1] = data[0]


    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")




# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End
