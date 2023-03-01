clothes = input().split(' ')
capacity = int(input())
current_capacity = capacity
racks = 1

while len(clothes) > 0:
    clothe = int(clothes.pop())
    if current_capacity >= clothe:
        current_capacity -= clothe
    else:
        racks += 1
        current_capacity = capacity
        current_capacity -= clothe

print(racks)