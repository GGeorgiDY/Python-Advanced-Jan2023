# като инпут ще ти се подава някакъв път до дадена папка (може да е "." -  сегашната траектория, или друга примерно ./files)
# след това ти трябва да вземеш всички файлове, от първо ниво (тоест без папките и файловете в тях) и да ги изпечаташ сортирани
# в някакъв файл първо екстеншъна (вида на файла) и след това имената на файловете с този екстеншън

import os

directory = input()
# нещо, което да ни пази екстеншъните
extensions = {}

# връща нещата които имаме в текущата папка без нивата надолу
for filename in os.listdir(directory):
# print(os.listdir(directory))
# ['1. Even Lines.py', '2. Line Numbers.py', '3. File Manipulator.py', '4. Directory Traversal.py', 'files']
    file = os.path.join(directory, filename)# така взимаме траекторията към дадения файл
    # print(file, end=' ')
# .\1. Even Lines.py .\2. Line Numbers.py .\3. File Manipulator.py .\4. Directory Traversal.py .\files

    if os.path.isfile(file):# проверяваме дали е файл
        extension = filename.split('.')[-1]
        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(filename)
    # print(extensions)
# {'py': ['1. Even Lines.py', '2. Line Numbers.py', '3. File Manipulator.py', '4. Directory Traversal.py']}

extensions = sorted(extensions.items(), key=lambda x: x[0])# сортираме по ключ

with open("files/report.txt", "w") as file:

    for extension, files in extensions:
        file.write(f".{extension} \n")

        for f in sorted(files):
            file.write(f"- - - {f} \n")


# .

# ./files

# примерно решение
# .html
# - - - index.html
# .py
# - - - solution.py
# .txt
# - - - output.txt
# - - - text.txt