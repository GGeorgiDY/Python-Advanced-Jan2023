def sorting_cheeses(**kwargs):
    # сортираме по броя на сирената след което сортираме по азбучен ред самите сирена
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    # [('Camembert', [100, 100, 105, 500, 430]), ('Parmesan', [102, 120, 135]), ('Mozzarella', [50, 125])]
    result = ''

    # сортирай бройките на всяко сирене по количеството в низходящ ред
    for key, value in sorted_cheeses:
        sorted_value = sorted(value, reverse=True)
        result += key + '\n'
        result += '\n'.join(map(str, sorted_value)) + '\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
