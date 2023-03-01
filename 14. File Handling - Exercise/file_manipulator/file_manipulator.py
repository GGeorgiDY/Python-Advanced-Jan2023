from os import remove

while True:
    command = input()
    if command == "End":
        break

    command = command.split("-")
    action = command[0]
    file_name = command[1]

    if action == "Create":
        with open(f'files/{file_name}', 'w') as file:
            file.close()

    if action == "Add":
        content = command[2]
        with open(f'files/{file_name}', 'a') as file:
            file.write(f"{content}\n")

    if action == "Replace":
        old_string = command[2]
        new_string = command[3]
        try:
            with open(f'files/{file_name}', 'r') as file:
                text = file.readlines()
                for line in range(len(text)):
                    text[line] = text[line].replace(old_string, new_string)
                file = open(f'files/{file_name}', 'w')
                file.write(''.join(text))
                file.close()
        except FileNotFoundError:
            print("An error occurred")

    if action == "Delete":
        try:
            remove(f'files/{file_name}')
        except FileNotFoundError:
            print("An error occurred")

