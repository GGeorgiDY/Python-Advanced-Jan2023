# Трябва да направим функция която ни работи с речник и връща нешата сортирани по намаляващо количество.
# Ако количеството е равно,сортираме по по дължината на името намаляващо. Ако и това е равно сортираме по име.
def grocery_store(**kwargs):
    sorter_kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = ''
    for k, v in sorter_kwargs.items():
        result += f"{k}: {v}" + '\n'
    return result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

