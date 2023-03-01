# направи фибоначи последователност с размер на числото което получиш като инпут, и потърси дали друго число
# се намира в тази фибоначи последователност

from Advanced.utils.fibonacci import create, locate
from Advanced.utils.command_parser import parse_line

nums = []
while True:
    line = input()
    if line == "Stop":
        break
    command, arg = parse_line(line)
    if command == "Create":
        nums = create(arg)
        print(*nums, sep=' ')
    else:
        idx = locate(arg, nums)
        output = f"The number {arg} is not in the sequence if idx == -1 else The number {arg} is not in the {idx}"
        print(output)

# Create Sequence 10
# Locate 13
# Create Sequence 3
# Locate 10
# Stop
