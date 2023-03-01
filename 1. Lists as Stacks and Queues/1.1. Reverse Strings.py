#I Love Python е инпута ни
# text = list(input())
# result = []
# while len(text) > 0:
#     result.append(text.pop())
# print(' '.join(result))
#може да се реши и по горния начин

text = list(input())
while len(text) > 0:
    print(text.pop(), end= "")