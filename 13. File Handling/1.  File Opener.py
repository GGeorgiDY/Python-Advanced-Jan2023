# имаш файл в папката, който се казва text.txt.
# Отвори файла. Ако го намериш изпишим 'File found' а ако не изпиши 'File not found'

file_path = './text.txt'
try:
    file = open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

# ако искам да ми прочете какво има вътре в този файл
# try:
#     file = open(file_path, 'r')
#     print(file.read())
# except FileNotFoundError:
#     print('File not found')