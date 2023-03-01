import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level: #чрез first_level правим така че да не не гледа повече от 1 път
            # във вложена папка - т.е. няма да гледа във вложената във вложената папка.
            save_extensions(file, first_level=True)


directory = input()
extensions = {}
result = []
save_extensions(directory)
sorted_extensions = dict(sorted(extensions.items(), key=lambda x: (x[0], x[1])))
for k, v in sorted_extensions.items():
    result.append(f".{k}")
    for file in v:
        result.append(f"- - - {file}")

with open(f"files/report.txt", "w") as file:
    file.write("\n".join(result))


#.