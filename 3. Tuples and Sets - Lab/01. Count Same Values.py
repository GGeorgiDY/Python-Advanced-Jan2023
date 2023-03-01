numbers = tuple(map(float, input().split()))
# print(numbers)
# (-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0)

lst = []
for i in numbers:
    if i not in lst:
        lst.append(i)
        number_count = numbers.count(i)
        print(f"{i} - {number_count} times")

# може и така да се напише с речник
# counter_of_values = {value: numbers.count(value) for value in numbers}
# for k, v in counter_of_values.items():
#     print(f"{k} - {v} times")


# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3

