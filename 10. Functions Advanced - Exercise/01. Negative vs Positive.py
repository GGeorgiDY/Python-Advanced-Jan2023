def my_func(*args):
    sum_of_positive_numbers = 0
    sum_of_negative_numbers = 0
    for i in args:
        if int(i) > 0:
            sum_of_positive_numbers += int(i)
        else:
            sum_of_negative_numbers -= int(i)
    diff = sum_of_positive_numbers - sum_of_negative_numbers

    if diff > 0:
        result = str(-sum_of_negative_numbers) + '\n'
        result += str(sum_of_positive_numbers) + '\n'
        result += "The positives are stronger than the negatives"
        return result
    else:
        result = str(-sum_of_negative_numbers) + '\n'
        result += str(sum_of_positive_numbers) + '\n'
        result += "The negatives are stronger than the positives"
        return result

data = [int(x) for x in input().split()]
print(my_func(*data))

# 1 2 -3 -4 65 -98 12 57 -84

