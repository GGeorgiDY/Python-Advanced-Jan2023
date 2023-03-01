from os import linesep

# създай нов файл с определено име, в който файл напиши даден текст
file_path = './my_first_file.txt'
with open(file_path, 'w') as file:
    file.write('I just created my first file!')