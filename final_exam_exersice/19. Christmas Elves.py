from collections import deque

energy = deque(map(int, input().split()))
materials_in_a_box = deque(map(int, input().split()))

total_elves_energy = 0
total_made_toys = 0
counter = 0

while energy and materials_in_a_box:
    ok = False
    spend_energy = 0
    counter += 1
    current_energy = energy.popleft()
    needed_energy = materials_in_a_box.pop()

    while energy and current_energy < 5:
        total_elves_energy += current_energy
        current_energy = energy.popleft()
        if current_energy >= 5:
            ok = True
    if not energy and not ok:
        break

    if counter % 3 == 0:
        needed_energy *= 2
        spend_energy += current_energy

        if current_energy - needed_energy < 0:
            materials_in_a_box.append(needed_energy // 2)
            energy.append(current_energy * 2)

        else:
            if counter % 5 == 0:
                current_energy -= needed_energy
                spend_energy -= current_energy
                total_elves_energy += spend_energy
                energy.append(current_energy)

            else:
                current_energy -= needed_energy
                spend_energy -= current_energy
                total_elves_energy += spend_energy
                energy.append(current_energy + 1)
                total_made_toys += 2
        continue

    elif counter % 5 == 0:
        spend_energy += current_energy

        if current_energy - needed_energy < 0:
            materials_in_a_box.append(needed_energy)
            energy.append(current_energy * 2)

        else:
            current_energy -= needed_energy
            spend_energy -= current_energy
            total_elves_energy += spend_energy
            energy.append(current_energy)
        continue

    if current_energy - needed_energy < 0:
        materials_in_a_box.append(needed_energy)
        energy.append(current_energy * 2)
    else:
        current_energy -= needed_energy
        energy.append(current_energy + 1)
        total_made_toys += 1
        total_elves_energy += (current_energy - (current_energy - needed_energy))


print(f"Toys: {total_made_toys}")
print(f"Energy: {total_elves_energy}")
if energy:
    print(f"Elves left: {', '.join(map(str, energy))}")
elif materials_in_a_box:
    print(f"Boxes left: {', '.join(map(str, materials_in_a_box))}")

# 10 16 13 25
# 12 11 8

# 10 14 22 4 5
# 11 16 17 11 1 8

# 5 6 7
# 2 1 5 7 5 3
