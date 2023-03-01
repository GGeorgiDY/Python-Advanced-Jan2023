from re import findall


class NameTooShortError(Exception):
    pass


class MustContainSymbolsError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = [".com", ".bg", ".org", ".net"]
email = input()

while email != "End":
    try:
        if '@' not in email:
            raise MustContainSymbolsError("Email must contain @")

        elif len(findall(pattern_name, email.split('@')[0])[0]) != len(email.split('@')[0]):
            raise InvalidNameError("Email name should contain only letters, numbers, underscores and dots.")

        elif email.count("@") > 1:
            raise MoreThanOneAtSymbolError('Email should contain only one @!')

        elif len(findall(pattern_name, email.split('@')[0])[0]) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

        elif findall(pattern_domain, email.split('@')[1])[0] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

        print('Email is valid')
    except IndexError:
        print('Invalid Email')

    email = input()