from string import punctuation

output_file = open("files/output.txt", "w")

with open('files/text.txt', 'r') as file:
    text = file.readlines()

line_counter = 1
for line in text:
    count_of_letters = 0
    count_of_punctuation_marks = 0
    for ch in line:
        if ch.isalpha():
            count_of_letters += 1
        elif ch in punctuation:
            count_of_punctuation_marks += 1
    output_file.write(f"Line {line_counter}: {line[:-1]} ({count_of_letters })({count_of_punctuation_marks})\n")
    line_counter += 1
output_file.close()