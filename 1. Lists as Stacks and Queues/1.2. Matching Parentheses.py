# data = list(input())
# lst = []
# counter = 0
# for i in data:
#     if i == "(":
#         lst.append(counter)
#     elif i == ")":
#         print(f"{''.join(data[lst.pop():counter+1])}")
#     counter += 1
#може и като горния пример да се реши

data = input()
lst = []
for i in range(len(data)):
    ch = data[i]
    if ch == "(":
        lst.append(i)
    elif ch == ")":
        last_opening_bracket = lst.pop()
        expression = data[last_opening_bracket:i+1]
        print(expression)