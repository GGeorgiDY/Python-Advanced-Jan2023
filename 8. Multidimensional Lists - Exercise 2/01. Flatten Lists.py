# входните данни трябва да ги разделя по | и да взема събстринговете на обратно
line = input().split('|')# ['1 2 3 ', '4 5 6 ', '  7  88']
sub_lists = []
for sub_string in line[::-1]:
    sub_lists.extend(sub_string.split())

print(*sub_lists)

# 1 2 3 |4 5 6 |  7  88