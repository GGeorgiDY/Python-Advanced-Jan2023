# трябва да направим програма която отчита команди, докато не получим командата "End"
from os import remove

while True:
    command = input()
    if command == "End":
        break

    command = command.split("-")

    if command[0] == "Create":
        file = open(f"files/{command[1]}", "w")
        file.close()

    elif command[0] == "Add":
        with open(f"files/{command[1]}", "a") as file:
            file.write(f"{command[2]}\n")

    elif command[0] == "Replace":
        try:
            with open(f"files/{command[1]}", "r") as file:
                text = file.readlines() #получаваме списък със всеки един ред

            file = open(f"files/{command[1]}", "w")

            for i in range(len(text)):
                text[i] = text[i].replace(command[2], command[3])

            file.write(''.join(text))
            file.close()
        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            remove(f"files/{command[1]}")
        except FileNotFoundError:
            print("An error occurred")

# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End

