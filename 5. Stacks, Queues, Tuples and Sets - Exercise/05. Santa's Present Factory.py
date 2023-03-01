from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))
que = []

toys = {'Doll': {'magic': 150, 'crafted': 0},
             'Wooden train': {'magic': 250, 'crafted': 0},
             'Teddy bear': {'magic': 300, 'crafted': 0},
             'Bicycle': {'magic': 400, 'crafted': 0}}

while materials and magic:
    # нарочно го правя с флаг, за да проверява дали има няколко проедни 0.
    # по този начин ще изтрие всички поредни 0 докато стигне до число != 0
    flag = False
    if materials[-1] == 0:
        materials.pop()
        flag = True

    if magic[0] == 0:
        magic.popleft()
        flag = True

    if flag:
        continue

    product = materials[-1] * magic[0]
    if product == toys['Doll']['magic']:
        toys['Doll']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Wooden train']['magic']:
        toys['Wooden train']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Teddy bear']['magic']:
        toys['Teddy bear']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Bicycle']['magic']:
        toys['Bicycle']['crafted'] += 1
        materials.pop()
        magic.popleft()
    else:
        if product > 0:
            materials[-1] += 15
            magic.popleft()
        elif product < 0:
            # product = materials[-1] + magic[0]
            # materials.pop()
            # magic.popleft()
            # materials.append(product)
            materials.append(materials.pop() + magic.popleft())

# print(toys)
# {'doll': {'magic': 150, 'crafted': 0}, 'wooden_train': {'magic': 250, 'crafted': 0}, 'teddy_bear': {'magic': 300, 'crafted': 2}, 'bicycle': {'magic': 400, 'crafted': 1}}

if toys['Doll']['crafted'] > 0 and toys['Wooden train']['crafted'] > 0 or \
        toys['Teddy bear']['crafted'] > 0 and toys['Bicycle']['crafted'] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    # for i in range(len(materials)):
    #     que.append(str(materials.pop()))
    # print(f"Materials left: {', '.join(que)}")
    print(f"Materials left: {', '.join(list(map(str, materials[::-1])))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

# for k, v in sorted(toys.items()):
#     if v['crafted'] > 0:
#         print(f"{k}: {v['crafted']}")

for toy in sorted(toys):
    if toys[toy]['crafted'] > 0:
        print(f"{toy}: {toys[toy]['crafted']}")

