def get_name(names, letter):
    for name in names:
        if name.startswith(letter):
            return name


def age_assignment(*args, **kwargs):
    people = {}
    for k, v in kwargs.items():
        name = get_name(args, k)
        people[name] = v

    sorted_people = dict(sorted(people.items(), key=lambda x: x[0]))
    result = ''
    for k, v in sorted_people.items():
        result += f"{k} is {v} years old." + '\n'
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))