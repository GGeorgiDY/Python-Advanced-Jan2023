def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


command = {
    'name': 'Gosho',
    'age': 23,
    'town': 'Sofia'
}

print(get_info(**command))
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))