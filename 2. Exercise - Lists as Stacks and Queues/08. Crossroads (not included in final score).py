from collections import deque

green_window = int(input())
free_window = int(input())

total_cars = 0
cars = deque()

while True:
    info = input()
    if info == "END":
        break

    if info != "green":
        # ако нямаме залено, значи ще имаме кола, която ще апенднем в нашата опашка
        cars.append(info)
    else:
        current_green = green_window

        # докато сфетофара свете зелено и има коли
        while current_green > 0 and cars:
            car = cars.popleft()
            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1

print("Everyone is safe.")
print(f"{total_cars} total cars passed the crossroads.")

# 10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END

# 9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END







