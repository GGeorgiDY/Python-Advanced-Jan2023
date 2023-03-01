lines = int(input())
guests = set()

for i in range(lines):
    guest = input()
    guests.add(guest)

while True:
    guest = input()
    if guest == "END":
        break

    guests.remove(guest)

print(len(guests))
for guest in sorted(guests):
    print(guest)

# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END