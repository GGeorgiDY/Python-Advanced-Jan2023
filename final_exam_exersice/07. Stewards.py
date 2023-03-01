from collections import deque

sequence_of_seats = deque(input().split(', '))
first = deque(map(int, input().split(', ')))
second = deque(map(int, input().split(', ')))
rotations = 0
seat_matches = []

while True:
    if len(seat_matches) == 3 or rotations == 10:
        break

    rotations += 1
    f_number = first.popleft()
    s_number = second.pop()
    sum_of_numbers = f_number + s_number
    ascii_number = chr(sum_of_numbers)
    f_seat = str(f_number) + ascii_number
    s_seat = str(s_number) + ascii_number

    if f_seat in sequence_of_seats and f_seat not in seat_matches:
        seat_matches.append(f_seat)
        continue

    if s_seat in sequence_of_seats and s_seat not in seat_matches:
        seat_matches.append(s_seat)
        continue

    if s_seat not in sequence_of_seats and f_seat not in sequence_of_seats:
        second.appendleft(s_number)
        first.append(f_number)


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")



# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46

# 25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40
