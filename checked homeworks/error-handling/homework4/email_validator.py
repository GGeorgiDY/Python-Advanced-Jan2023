class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()

domain_list = ["com", "bg", "org", "net"]

while command != "End":

    try:
        if "@" not in command:
            raise MustContainAtSymbolError("Email must contain @")
        name, domain = command.split("@")
        if len(name) < 5:
            raise NameTooShortError("Name must be more than 4 characters")
        domain_check = command.split(".")
        if domain_check[-1] not in domain_list:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except KeyError:
        print("Try again")

    else:
        print("Email is valid")

    command = input()
