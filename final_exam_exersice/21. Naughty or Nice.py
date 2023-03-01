# def naughty_or_nice_list(santa_list, *args, **kwargs):
#     nice_or_naughty = {"Nice": [], "Naughty": []}
#
#     for data in args:
#         counting_numbers = [item[0] for item in santa_list]
#         number, status = data.split("-")
#         number = int(number)
#         if counting_numbers.count(number) == 1:
#             for kid_number, kid_name in santa_list:
#                 if kid_number == number:
#                     nice_or_naughty[status].append(kid_name)
#                     santa_list.remove((kid_number, kid_name))
#                     break
#
#     for name, stat in kwargs.items():
#         counting_names = [item[1] for item in santa_list]
#         if counting_names.count(name) == 1:
#             for kid_number, kid_name in santa_list:
#                 if name == kid_name:
#                     nice_or_naughty[stat].append(name)
#                     santa_list.remove((kid_number, kid_name))
#                     break
#
#     nice_or_naughty["Not found"] = [x[1] for x in santa_list]
#
#     result = ""
#
#     for status, kids in nice_or_naughty.items():
#         if kids:
#             result += f"{status}: {', '.join(kids)}\n"
#
#     return result.strip()

def naughty_or_nice_list(kids, *args, **kwargs):
    sorted_kids = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }

    if args:
        for command in args:
            counting_number = 0
            found_name = []
            number, kid_type = command.split('-')
            kid_to_remove = 0

            for kid_info in kids:
                kid_number, name = kid_info

                if int(number) == kid_number:
                    counting_number += 1
                    found_name.append(name)
                    kid_to_remove = kids.index(kid_info)

            if counting_number == 1:
                sorted_kids[kid_type].append(found_name.pop())
                kids.pop(kid_to_remove)

    if kwargs:
        for name, kid_type in kwargs.items():
            counting_number = 0
            found_name = []

            for kid_info in kids:
                kid_name = kid_info[1]

                if kid_name == name:
                    counting_number += 1
                    found_name.append(name)
                    kid_to_remove = kids.index(kid_info)

            if counting_number == 1:
                sorted_kids[kid_type].append(found_name.pop())
                kids.pop(kid_to_remove)

    if kids:
        for num, non_found_kid in kids:
            sorted_kids['Not found'].append(non_found_kid)

    result = ''
    for kid_type, kids in sorted_kids.items():
        if kids:
            result += f'{kid_type}: {", ".join(kids)}\n'

    return result



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))
