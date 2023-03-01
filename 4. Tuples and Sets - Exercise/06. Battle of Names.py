import math
n = int(input())
counter = 1
value = 0
odd_set = set()
even_set = set()

for _ in range(n):
    name = input()
    for ch in name:
        value += ord(ch)
    result = math.floor(value / counter)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
    counter += 1
    value = 0

# print(odd_set) {511}
# print(even_set) {304, 128, 206}

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)


if sum_even_set == sum_odd_set:
    result = even_set.union(odd_set)
elif sum_even_set < sum_odd_set:
    result = odd_set.difference(even_set)
else:
    result = even_set.symmetric_difference(odd_set)

print(f"{', '.join(str(i) for i in result)}")


# 4
# Pesho
# Stefan
# Stamat
# Gosho

# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan

