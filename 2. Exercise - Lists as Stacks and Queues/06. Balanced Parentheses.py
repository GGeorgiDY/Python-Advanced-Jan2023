result = True
parentheses = input()
stack = []

for i in parentheses:
    if i in ['(', '{', '[']:
        stack.append(i)

    elif i == ')':
        if stack and stack[-1] == '(':
            if stack:
                stack.pop()
        else:
            result = False
            break

    elif i == '}':
        if stack and stack[-1] == '{':
            if stack:
                stack.pop()
        else:
            result = False
            break

    elif i == ']':
        if stack and stack[-1] == '[':
            if stack:
                stack.pop()
        else:
            result = False
            break

print("YES" if result else "NO")