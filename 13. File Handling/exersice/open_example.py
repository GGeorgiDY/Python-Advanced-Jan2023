# file2 = open('open_example.py')
# print(file2.readlines())
# ["file2 = open('open_example.py')\n", 'print(file2.readlines())\n']

# print(file2.read())
# file2 = open('open_example.py')
# # print(file2.readlines())
# # ["# file = open('Advanced/13. File Handling/exersice/open_example.py')\n", "file2 = open('open_example.py')\n", 'print(file2.readlines())\n']

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# open('example-1.txt', 'w')
# with open('example-1.txt', 'w') as file:
#     file.write('Python language\n')
#     file.write('Hello SoftUni')
#
# open('example-2.txt', 'a')
# with open('example-2.txt', 'a') as file:
#     file.write('Python language\n')
#     file.write('Hello SoftUni')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# some_file = open('example-1.txt')
# print(some_file.read(7)) #чете първите 7 знака
# print(some_file.read(7)) #чете следващите 7 знака

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# some_file2 = open('example-1.txt')
# while True:
#     current_text = some_file2.readline() #така принтира целия ред и оставя един празен ред разтояние. Ако вътре в
#     # скобите подам 3 ще принтира първите 3 символа от всеки ред
#     print(current_text)
#     if not current_text:
#         break

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# some_file3 = open('example-2.txt')
# while True:
#     current_text = some_file3.readlines() #връща списък с разделение между отделните редове
#     print(current_text)
#     if not current_text:
#         break

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # връща ми всеки ред като списък и всяка дума е отделен елемент в списъка
# with open('example-2.txt', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         data = line.split()
#         print(data)
#
# # ['Python', 'language']
# # ['Hello', 'SoftUniPython', 'language']
# # ['Hello', 'SoftUni']

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # прави същото като горния пример
# some_file = open('example-2.txt', 'r')
# for line in some_file:
#     data = line.split()
#     print(data)
#
# # ['Python', 'language']
# # ['Hello', 'SoftUniPython', 'language']
# # ['Hello', 'SoftUni']

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # може и като си направим функция -> ще се изпълни същото като горните 2 примера
# def read_file_row_by_row(file_name):
#     some_file = open(file_name, 'r')
#     for line in some_file:
#         data = line.split()
#         print(data)
#
#
# read_file_row_by_row('example-2.txt')
#
# # ['Python', 'language']
# # ['Hello', 'SoftUniPython', 'language']
# # ['Hello', 'SoftUni']

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # създаваме файл и пишем в него на нов ред всеки елемент от Lines
# lines = ['Readme', 'This is my GitHub repository']
# with open('readme.txt', 'w') as file:
#     for line in lines:
#         file.write(line)
#         file.write('\n')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # добавяме нови неща във вече създадения файл (работи и когато нямаме създаден файл - тогава ще го създаде)
# more_lines = ['', 'Append text files', 'The End!']
# with open('readme.txt', 'a') as file:
#     file.write('\n'.join(more_lines))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def write_data_to_file(file, mode):
#     current_file = open(file, mode)
#     current_file.write('''This is just example!!!:\n
# First line,
# Second line,
# Third line.
# End of example!''')
#
#
# write_data_to_file('new_file_example', 'w')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # вариант в който използваме и with и close
# class MessageWritter(object):
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def __enter__(self):
#         self.file_name = open(self.file_name, 'w')
#         return self.file_name
#
#     def __exit__(self, *args):
#         self.file_name.close()
#
#
# with MessageWritter('SoftUni.txt') as file:
#     file.write('Hello SoftUni \nClass Example!')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import os

# връща работната ни директория
# print(os.getcwd())

# създаваме работна директория (в този случай създава нова папка 'exersice 2'
# print(os.mkdir('C:/Users/L560/PycharmProjects/firstSteps/Advanced/13. File Handling/exersice2'))

# създава нова папка 'Workshop2' в текущата директория
# os.getcwd()
# os.mkdir('Workshop2')

# изтрива файл 'asd.txt'
# os.remove('asd.txt')

# връща списък със съдържанието в текущата директория (всеки файл в директорията е отделен елемент)
# print(os.listdir(os.getcwd()))

# изтрива даден файл ако съществува
# file_path = 'readme.txt '
# if os.path.exists(file_path):
#     os.remove(file_path)