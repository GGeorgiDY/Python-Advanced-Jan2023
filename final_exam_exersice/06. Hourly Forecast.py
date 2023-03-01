def forecast(*args):
    my_dict = {}
    result = ''
    for i in args:
        location, weather = i[0], i[1]
        if location not in my_dict:
            if weather == "Sunny":
                my_dict[location] = [weather, 1]
            if weather == "Cloudy":
                my_dict[location] = [weather, 2]
            if weather == "Rainy":
                my_dict[location] = [weather, 3]
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (x[1][1], x[0])))
    for k, v in sorted_dict.items():
        result += f"{k} - {v[0]}" + '\n'
    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
