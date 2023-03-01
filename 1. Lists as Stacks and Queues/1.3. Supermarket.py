from collections import deque

people = deque()
while True:
    command = input()
    if command == 'End':
        break

    if command == "Paid":
        print('\n'.join(people))
        people.clear()
    else:
        people.append(command)

print(f"{len(people)} people remaining.")

# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End
