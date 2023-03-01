def math_operations(*args, **kwargs):
    for i in range(len(args)):
        key = list(kwargs.keys())[i % 4] #[a, s, d, m]

        if key == "a":
            kwargs[key] += args[i]

        if key == "s":
            kwargs[key] -= args[i]

        if key == "d":
            if args[i] != 0:
                kwargs[key] /= args[i]

        if key == "m":
            kwargs[key] *= args[i]

    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    return '\n'.join(f"{k}: {v:.1f}" for k, v in sorted_kwargs.items())


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

# a = 0 % 4
# b = 1 % 4
# c = 2 % 4
# d = 3 % 4
# e = 4 % 4
# f = 5 % 4
#
# print(a, b, c, d, e, f) #0 1 2 3 0 1