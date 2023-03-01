# text = input()
#
# # за да работи правилно times съм го сложил във try
# try:
#     times = int(input())
#     output = text * times
#     print(output)
# except ValueError:
#     print("Variable times must be integer")

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\\

# def repeat_text(text, number):
#    return text * number
#
#
# try:
#     text = input()
#     number = int(input())
#     print(repeat_text(text, number))
# except ValueError:
#     print("Variable times must be integer")

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

from io import StringIO
import sys

test_input = '''Hello SoftUni 
2'''
# чрез stdin може да получаваме input от дадена променлива в кода
sys.stdin = StringIO(test_input)


def repeat_text(text, number):
   return text * number


try:
    text = input()
    number = int(input())
    print(repeat_text(text, number))
except ValueError:
    print("Variable times must be integer")