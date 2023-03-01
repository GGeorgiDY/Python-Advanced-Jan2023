lines = int(input())
cars = set()

for i in range(lines):
    command = input().split(', ')
    action = command[0]
    car = command[1]
    if action == "IN":
        cars.add(car)
    else:
        cars.remove(car)

if len(cars) > 0:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU
