from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

my_dict = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while len(textiles) > 0 and len(medicaments) > 0:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    result = current_textile + current_medicament

    if result == 30:
        my_dict['Patch'] += 1
    elif result == 40:
        my_dict['Bandage'] += 1
    elif result == 100:
        my_dict['MedKit'] += 1

    else:
        if result > 100:
            my_dict['MedKit'] += 1
            if len(medicaments) > 0:
                new_medicament = medicaments.pop()
                new_medicament += (result - 100)
                medicaments.append(new_medicament)
        else:
            current_medicament += 10
            medicaments.append(current_medicament)


sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
if len(medicaments) == 0 and len(textiles) == 0:
    print("Textiles and medicaments are both empty.")
    for k, v in sorted_dict.items():
        if v > 0:
            print(f"{k} - {v}")
else:
    if len(textiles) == 0:
        print("Textiles are empty.")
        for k, v in sorted_dict.items():
            if v > 0:
                print(f"{k} - {v}")
        medicaments.reverse()
        print(f"Medicaments left: {', '.join(map(str, medicaments))}")
    else:
        print("Medicaments are empty.")
        for k, v in sorted_dict.items():
            if v > 0:
                print(f"{k} - {v}")
        print(f"Textiles left: {', '.join(map(str, textiles))}")







