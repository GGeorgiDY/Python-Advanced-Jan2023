def operate(operator, *args):
    def add():
        return sum(args)

    def substraction():
        result = 0
        for i in args:
            result -= i
        return result

    def division():
        counter = 0
        for i in args:
            if counter == 0:
                result = i
                counter += 1
            result /= i
        return result

    def multiplication():
        result = 1
        for i in args:
            result *= i
        return result

    if operator == '+':
        return add()
    elif operator == '-':
        return substraction()
    elif operator == '*':
        return multiplication()
    elif operator == '/':
        return division()



print(operate("-", 1, 2, 3))
print(operate("/", 3, 4))