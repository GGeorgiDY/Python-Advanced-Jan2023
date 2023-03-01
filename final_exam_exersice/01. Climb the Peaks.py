from collections import deque

daily_portions = deque(map(int, input().split(', ')))
quantities_of_daily_stamina = deque(map(int, input().split(', ')))
mountain_peaks = {1: ["Vihren", 80], 2: ["Kutelo", 90], 3: ["Banski Suhodol", 100], 4: ["Polezhan", 60], 5: ["Kamenitza", 70]}
conquered_peaks = []
counter = 1
# print(mountain_peaks[counter][1])
# mountain_peaks.pop(counter)
# counter = counter + 1
# print(mountain_peaks[counter][1])

while daily_portions and quantities_of_daily_stamina and mountain_peaks:
    daily_portion = daily_portions.pop()
    daily_stamina = quantities_of_daily_stamina.popleft()
    daily_power = daily_portion + daily_stamina
    if not mountain_peaks:
        break
    if daily_power >= mountain_peaks[counter][1]:
        conquered_peaks.append(mountain_peaks[counter][0])
        mountain_peaks.pop(counter)
        counter += 1

if not mountain_peaks:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    if len(conquered_peaks) > 0:
        print("Conquered peaks:")
        print('\n'.join(conquered_peaks))
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if len(conquered_peaks) > 0:
        print("Conquered peaks:")
        print('\n'.join(conquered_peaks))


# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2