# shopping_list = {}
#
#
# def show_list(shopping_list, include_quantities=True):
#     print()
#     for item_name, quantity in shopping_list.items():
#         if include_quantities:
#             print(f'{quantity} x {item_name}')
#         else:
#             print(item_name)
#
#
# def add_items(shopping_list, **things_to_buy):
#     for item_name, quantity in things_to_buy.items():
#         shopping_list[item_name] = quantity
#     return shopping_list
#
# shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
# show_list(shopping_list, include_quantities=True)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def multiply(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result
#
# print(multiply(4, 5, 6, 1, 3))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def get_info(name, age, town):
    return f'This is {name} from {town} and he is {age} years old'


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))