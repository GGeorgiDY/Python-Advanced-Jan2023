def concatenate(*args, **kwargs):
    # lst = []
    # for i in args:
    #     lst.append(i)
    # result = ''.join(lst)
    result = ''.join(args)
    for k, v in kwargs.items():
        if k in result:
            result = result.replace(k, v)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))