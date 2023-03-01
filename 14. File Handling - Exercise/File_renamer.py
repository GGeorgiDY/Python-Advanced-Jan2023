import os
import re

directory = input("Enter directory: ")
string_to_replace = input("Enter the string you want to replace: ")
string_to_replace_with = input("Enter the string you want to replace with: ")

for filename in os.listdir(directory): # връща нещата които имаме в текущата папка без нивата надолу
    file = os.path.join(directory, filename) # така взимаме траекторията към дадения файл

    if os.path.isfile(file):
        new_name = filename.replace(string_to_replace, string_to_replace_with)
        new_file = "/".join(re.split(r'[\\/]', file)[:-1]) + "/" + new_name

        os.rename(file, new_file)
