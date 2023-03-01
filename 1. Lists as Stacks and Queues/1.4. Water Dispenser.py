from collections import deque

quantity = int(input())
people = deque()
while True:
    command = input()
    if command == 'Start':
        break
    people.append(command)

while True:
    command = input()
    if command == 'End':
        break

    if 'refill' in command:
        command = command.split()
        added_water = command[1]
        quantity += int(added_water)
    else:
        if int(command) <= quantity:
            quantity -= int(command)
            name = people.popleft()
            print(f"{name} got water")
        else:
            name = people.popleft()
            print(f"{name} must wait")

print(f"{quantity} liters left")