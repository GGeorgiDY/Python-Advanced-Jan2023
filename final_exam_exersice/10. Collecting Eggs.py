# from collections import deque
#
# egg_with_its_size = deque(map(int, input().split(', ')))
# a_piece_of_paper_with_its_size = deque(map(int, input().split(', ')))
# box_size = 50
# filled_box_counter = 0
#
#
# while egg_with_its_size and a_piece_of_paper_with_its_size:
#     if egg_with_its_size[0] == 13:
#         egg_with_its_size.popleft()
#         first_paper = a_piece_of_paper_with_its_size.popleft()
#         last_paper = a_piece_of_paper_with_its_size.pop()
#         a_piece_of_paper_with_its_size.append(first_paper)
#         a_piece_of_paper_with_its_size.appendleft(last_paper)
#     if len(egg_with_its_size) == 0:
#         break
#
#     elif egg_with_its_size[0] <= 0:
#         egg_with_its_size.popleft()
#         continue
#
#     current_egg = egg_with_its_size.popleft()
#     current_paper = a_piece_of_paper_with_its_size.pop()
#
#     if current_egg + current_paper <= box_size:
#         filled_box_counter += 1
#
# if filled_box_counter > 0:
#     print(f"Great! You filled {filled_box_counter} boxes.")
# else:
#     print(f"Sorry! You couldn't fill any boxes!")
#
# if len(egg_with_its_size) > 0:
#     print(f"Eggs left: {', '.join(map(str, egg_with_its_size))}")
#
# if len(a_piece_of_paper_with_its_size) > 0:
#     print(f"Pieces of paper left: {', '.join(map(str, a_piece_of_paper_with_its_size))}")

# горния код минаваше на 88% поради грешка Run time error
# долния код не е с deque и за това е по-бърз и за това минава на 100%

eggs_sizes = [int(x) for x in input().split(", ")]
paper_sizes = [int(x) for x in input().split(", ")]

box_size = 50
boxes = 0

while eggs_sizes and paper_sizes:
    egg = eggs_sizes[0]
    paper = paper_sizes[-1]
    if egg <= 0:
        eggs_sizes.pop(0)
        continue
    if egg == 13:
        eggs_sizes.pop(0)
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue

    if egg + paper <= box_size:
        boxes += 1
    eggs_sizes.pop(0)
    paper_sizes.pop()

if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if len(eggs_sizes) > 0:
    print(f'Eggs left: {", ".join(str(x) for x in eggs_sizes)}')
if len(paper_sizes) > 0:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper_sizes)}')


