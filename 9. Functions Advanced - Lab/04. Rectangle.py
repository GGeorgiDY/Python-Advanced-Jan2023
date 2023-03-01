def rectangle(lenght, width):
    def area():
        return f'Rectangle area: {lenght * width}'

    def perimeter():
        return f'Rectangle perimeter: {lenght*2 + width*2}'

    # тук проверяваме дали подадените дължина и ширина са int, иначe връща 'Enter valid values!'
    if not isinstance(width, int) or not isinstance(lenght, int):
        return 'Enter valid values!'
    return area() + '\n' + perimeter()


print(rectangle(2, 10))
