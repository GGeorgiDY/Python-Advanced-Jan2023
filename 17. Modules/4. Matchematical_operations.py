# да направим модул, който изпълнява базови калкулации като получаваме 2 числа и знак между тях
from Advanced.utils.match_operations import calculate_expression

first, operator, second = input().split()
calculate_expression(float(first), float(second), operator)



# 2.5 * 2