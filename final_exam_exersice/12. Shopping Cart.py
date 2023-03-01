def shopping_cart(*args):
    cart_dict = {"Soup": [], "Pizza": [], "Dessert": []}
    result = ''
    for elements in args:
        if elements == "Stop":
            break

        meal, product = elements[0], elements[1]

        if meal == 'Soup' and len(cart_dict['Soup']) < 3 and product not in cart_dict['Soup']:
            cart_dict[meal].append(product)

        elif meal == 'Pizza' and len(cart_dict['Pizza']) < 4 and product not in cart_dict['Pizza']:
            cart_dict[meal].append(product)

        elif meal == 'Dessert' and len(cart_dict['Dessert']) < 2 and product not in cart_dict['Dessert']:
            cart_dict[meal].append(product)

    if len(cart_dict['Soup']) == 0 and len(cart_dict['Pizza']) == 0 and len(cart_dict['Dessert']) == 0:
        return f"No products in the cart!"

    sorted_dict = dict(sorted(cart_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, v in sorted_dict.items():
        result += f'{k}:' + '\n'
        for product in sorted(v):
            result += f" - {product}" + '\n'
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
