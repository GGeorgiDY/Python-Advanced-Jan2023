numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

searched_number = input()
while searched_number != "Remove":
    try:
        print(numbers_dictionary[searched_number])
    except KeyError:
        print("Number does not exist in dictionary")
    searched_number = input()


removed_number = input()
while removed_number != "End":
    try:
        del numbers_dictionary[removed_number]
    except KeyError:
        print("Number does not exist in dictionary")
    removed_number = input()

print(numbers_dictionary)

# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End

# one
# two
# Search
# Remove
# End

# one
# 1
# Search
# one
# Remove
# two
# End
