from collections import deque

milligrams_of_caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
maximum_milligrams_of_caffeine = 300

while len(milligrams_of_caffeine) > 0 and len(energy_drinks) > 0:
    caffeine = milligrams_of_caffeine[-1]
    drink = energy_drinks[0]
    total_coffeine = caffeine * drink
    if maximum_milligrams_of_caffeine >= total_coffeine:
        maximum_milligrams_of_caffeine -= total_coffeine
        milligrams_of_caffeine.pop()
        energy_drinks.popleft()
    else:
        milligrams_of_caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        maximum_milligrams_of_caffeine += 30
        if maximum_milligrams_of_caffeine > 300:
            maximum_milligrams_of_caffeine = 300

if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {300 - maximum_milligrams_of_caffeine} mg caffeine.")