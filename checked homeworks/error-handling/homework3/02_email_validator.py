import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


minimum_length = 4
pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = [".com", ".bg", ".org", ".net"]

email = input()
while email != "End":
    try:
        if email.count("@") > 1:
            raise MoreThanOneAtSymbol("Email must contain only one @ sign")
        if len(email.split("@")[0]) <= minimum_length:
            raise NameTooShortError(f"Name must be more than {minimum_length} characters")
        if re.findall(pattern_name, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name can only contain alphanumeric characters, underscores and dots")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if re.findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")


    except IndexError:
        print("Invalid Email")

    else:
        print("Email is valid")

    email = input()
