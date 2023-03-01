def even_odd_filter(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        if k == 'even':
            result = [x for x in v if x % 2 == 0]
            my_dict['even'] = result
        elif k == 'odd':
            result = [x for x in v if x % 2 != 0]
            my_dict['odd'] = result

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
