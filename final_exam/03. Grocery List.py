def shop_from_grocery_list(budget, grocery_list, *args):
    my_dict = {}
    bulean = False
    result = ''
    my_set = []
    for i in grocery_list:
        my_dict[i] = 0

    for product, price in args:
        if bulean:
            break
        if product in my_dict and my_dict[product] == 0:
            if budget - price >= 0:
                budget -= price
                my_dict[product] += 1
                my_set.append(product)
            else:
                bulean = True

    if len(grocery_list) == len(my_set):
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        grocery_list = set(grocery_list)
        my_set = set(my_set)
        missing_products = grocery_list - my_set
        result += f"You did not buy all the products. Missing products: {', '.join(missing_products)}."

    return result

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
