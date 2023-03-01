def numbers_sum(file_name):
    data = open(file_name, 'r')
    sum_numbers = 0

    for number in data:
        sum_numbers += int(number)

    return sum_numbers


print(numbers_sum('text.txt'))