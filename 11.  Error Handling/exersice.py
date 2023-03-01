# def sum_even_numbers(nums):
#     even_numbers = 0
#
#     for num in nums:
#         if num % 2 == 0:
#             even_numbers += num
#         elif num % 2 != 1:
#             continue
#         else:
#             raise ValueError
#
# try:
#     sum_even_numbers(['9', 5, 8])
# except:
#     print("Exception handled")
# finally:
#     print("This is finally")

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\

# def hello():
#     print('Hello SoftUni')
#
# try:
#     hello()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause')

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def hello():
#     raise AssertionError
#
# try:
#     hello()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause')

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class CustomsException(Exception):
#     pass
#
#
# try:
#     raise CustomsException('This is my custom exception')
# except CustomsException as error:
#     print(error)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
from unittest import result


class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The {self.f} is not in a valid range {self.min_f, self.max_f}"


def fahrenheit_to_celsius(f: float) -> float:
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)
    return (f - 32) * 5 / 9


value = input('Enter a temperature in Fahrenheit: ')
try:
    f = float(value)
except ValueError as error:
    print(error)
else:
    try:
        result = fahrenheit_to_celsius(float(f))
    except FahrenheitError as error:
        print(error)
    else:
        print(f'{f} Fahrenheit = {result:.4f} Celsius')