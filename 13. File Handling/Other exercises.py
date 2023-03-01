# file_path = './text.txt'
# try:
#     file = open(file_path, 'r')
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)
# except FileNotFoundError:
#     print("File not found")

# ще ми принтира
# This is some random line
#
# This is the second line
#
# And this is the third line
#

#////////////////////////////////////////////////////////////////////////////////////////////

# file_path = './text.txt'
# try:
#     file = open(file_path, 'r')
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())
# except FileNotFoundError:
#     print("File not found")

# ще изпринти
# This is some random line
# This is the second line
# And this is the third line

#////////////////////////////////////////////////////////////////////////////////////////////

# file_path = './text.txt'
# try:
#     file = open(file_path, 'r')
#     print(file.readlines())
# except FileNotFoundError:
#     print("File not found")

# ще изпринти
# ['This is some random line\n', 'This is the second line\n', 'And this is the third line']

#////////////////////////////////////////////////////////////////////////////////////////////

# Ако искам да създам файл, който да се казва output.txt и да съдържа в себе си надписа Hello World
# file_path = './output.txt'
# file = open(file_path, 'w')
# file.write('Hello world')
# file.write('Hello world again')

#////////////////////////////////////////////////////////////////////////////////////////////

# как се затваря файл
# file_path = './output.txt'
# file = open(file_path, 'a')
# config = file.read() #четеш си файла (не е задължително да го правиш, дадено е като пример)
# file.close() # затваряш файла

#////////////////////////////////////////////////////////////////////////////////////////////

# отваряне и затваряне на файл с with
# file_path = './output.txt'
# with open(file_path, 'r') as file:
#     print(file.read(4))

#////////////////////////////////////////////////////////////////////////////////////////////

# така можем да добавяме на първия ред във файла дадена информация и да го запазим (подпъхваме текс в текста)
# file_path = './output.txt'
# new_content = ''
# with open(file_path, 'r+') as file:
#     original_content = file.read()
#     new_content = "placeholder text: " + original_content
#     file.seek(0)
#     file.truncate(0)
#     file.write(new_content)

#////////////////////////////////////////////////////////////////////////////////////////////

# изтрий даден файл
# from os import remove
# try:
#     remove('./somefile.txt')
# except FileNotFoundError:
#     print('File does not exist')

#////////////////////////////////////////////////////////////////////////////////////////////

# да проверим дали даден файл съществува
# from os import path, remove
# file_path = './demo.txt'
# print(path.exists(file_path)) # ще върне True защото го има
# remove(file_path) # ще го изтрие
# print(path.exists(file_path)) # ще върне False, защото вече го няма

# или
# from os import path, remove
# file_path = './demo.txt'
# if path.exists(file_path):
#     remove(file_path)
#     print('File has been removed')
# else:
#     print('File does not exist')

#////////////////////////////////////////////////////////////////////////////////////////////

# праименувай файл
# from os import rename, path
# dir_path = './13. File Handling'
# old_file_name = 'demo.txt'
# new_file_name = 'new_demo.txt'
# rename(path.join(dir_path, old_file_name), path.join(dir_path, new_file_name))
