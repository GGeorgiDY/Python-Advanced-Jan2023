class NameTooShortError(Exception):
    # Name must be more than 4 characters
    pass


class MustContainAtSymbolError(Exception):
    # Email must contain @
    pass


class InvalidDomainError(Exception):
    # Domain must be one of the following: .com, .bg, .org, .net
    pass


valid_domains = [".com", ".bg", ".org", ".net"]

email = input()

while email != "End":
    try:
        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if email.split('.')[-1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except IndexError:
        print("Invalid email!")

    else:
        print("Email is valid")

    email = input()
