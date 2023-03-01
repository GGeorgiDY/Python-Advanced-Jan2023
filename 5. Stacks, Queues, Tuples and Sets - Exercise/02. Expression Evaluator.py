from functools import reduce
#
# line = input().split()
# stack = []
#
# for ch in line:
#     if ch.lstrip('-').isnumeric():#проверяваме дали е число, като включваме и да проверява дали е отрицателно
#         stack.append(int(ch))
#     else:
#         if ch == '*':
#             stack = [reduce(lambda x, y: x * y, stack)]
#         elif ch == '/':
#             stack = [reduce(lambda x, y: x // y, stack)]
#         elif ch == '+':
#             stack = [reduce(lambda x, y: x + y, stack)]
#         elif ch == '-':
#             stack = [reduce(lambda x, y: x - y, stack)]
#
# print(*stack)

expression = input().split()
idx = 0
# reduce взима една кофа пълна с елементи (в нашия случай списък) и ще извика една ламбда която има два параметъра a и b
# и ще върне резултата от а*b. Този резултат ще се върне обратно в кофата (в списъка) в нейното начало. Това ще продължи
# докато сме му казали (а ние му казахме да го прави до expression[:i]). Заключение: ако вътре в кофата към момента имаме
# 3 числа [2, 3, 4], първо ще се умножи 2 * 3 и ще върне 6, което ще дойде обратно като първи елемент в списъка и после
# ще умножи 6 * 4 и ще върне числото 24, което ще застане като първи елемент в списъка.
functions = {
    # i в lambda се взима от idx
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
}

while idx < len(expression):
    element = expression[idx]

    if element in "*/+-":
        # слагай кръгли скоби за да извикаш функцията
        result = functions[element](idx)
        # сега трябва да изчистим нашия експрешън и да вмъкнем резултата
        [expression.pop(1) for i in range(idx)]
        expression[0] = result
        # нулираме индекса, за да не пропуснем числа, които трябва да смятам
        idx = 0

    idx += 1

print(int(expression[0]))