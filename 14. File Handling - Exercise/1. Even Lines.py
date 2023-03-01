# четем текстов файл с редове. Принтираме четните редове на конзолата, като преди това определени символи сме
# ги заменили с @
symbols = ['-', ',', '.', '!', '?']

# първо трябва да си прочетем файла
with open("files/text.txt", 'r') as even_lines_file:
    text = even_lines_file.readlines()
# print(text)
# ["- I was quick to judge him, but it wasn't his fault.\n",
# '- Is this some kind of joke?! Is it?\n',
# '- Quick, hide here... It is safer\n']

for row in range(0, len(text), 2):
    # сега трябва да заменим символите
    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    # сега трябва да си обърнем думите в изречението и да ги принтираме
    print(*text[row].split()[::-1], sep=' ')