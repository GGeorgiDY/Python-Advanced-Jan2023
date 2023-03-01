# def my_func(*args):
#     positive_numbers = 0
#     negative_numbers = 0
#     positive_numbers = sum(x for x in args if x > 0)
#     negative_numbers = sum(x for x in args if x < 0)
#     print(negative_numbers)
#     print(positive_numbers)
#
#     diff = positive_numbers - abs(negative_numbers)
#     if diff > 0:
#         print("The positives are stronger than the negatives")
#     else:
#         print("The negatives are stronger than the positives")
#
#
# data = [int(x) for x in input().split()]
# my_func(*data)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def even_odd_filter(**kwargs):
#     my_dict = {}
#     for k, v in kwargs.items():
#         if k == "odd":
#             result = [x for x in v if x % 2 != 0]
#             my_dict[k] = result
#         if k == "even":
#             result = [x for x in v if x % 2 == 0]
#             my_dict[k] = result
#     return dict(sorted(my_dict.items(), key=lambda x: -len(x[1])))
#
#
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def grocery_store(**kwargs):
#     my_dict= {}
#     for name, quantity in kwargs.items():
#         my_dict[name] = quantity
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
#     result = ''
#     for k, v in sorted_dict.items():
#         result += f"{k}: {v}" + '\n'
#     return result
#
#
#
# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
#
# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def age_assignment(*args, **kwargs):
#     result = ''
#     my_dict = {}
#     for i in args:
#         my_dict[i[0]] = i
#
#     sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))
#
#     for name, age in sorted_kwargs.items():
#         if name in my_dict:
#             result += f"{my_dict[name]} is {age} years old." + '\n'
#     return result
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def palindrome(name, idx):

    if idx == len(name):
        return f"{name} is palindrome"

    first_letter, last_letter = name[idx], name[len(name)-1-idx]
    if first_letter != last_letter:
        return f"{name} is not a palindrome"

    idx += 1
    return palindrome(name, idx)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))