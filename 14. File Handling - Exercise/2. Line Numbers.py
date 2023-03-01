# четем текстов файл и инсъртваме преди всеки ред line numbers като в края слагаме броя на всички букви и пункт знаци
# резултата трябва да го напишем в друг файл

from string import punctuation
# print(punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ принтва всички пунктуационни знаци

output_file = open("files/output.txt", "a")

with open("files/text.txt", 'r') as text_file:
    text = text_file.readlines() # прочитаме си редовете

for i in range(len(text)):
    row = text[i] #взимаме си всеки ред
    letters = 0
    marks = 0
    for symbol in row:
        if symbol.isalnum():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(row[:-1])} ({letters}) ({marks})\n")

output_file.close()
