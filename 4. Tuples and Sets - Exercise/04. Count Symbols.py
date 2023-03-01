word = input()
my_dict = {}

for ch in word:
    if ch not in my_dict:
        my_dict[ch] = 1
    else:
        my_dict[ch] += 1

for i in sorted(my_dict.keys()):
    print(f"{i}: {my_dict[i]} time/s")

# SoftUni rocks