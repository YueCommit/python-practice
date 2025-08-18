empty_dict = {}
print(type(empty_dict))

product_prices = {
    'creamer': 3.79,
    'apples': 3.99,
    'pears': 3.99,
}

product_keys = product_prices.keys()
print(product_keys)

product_values = product_prices.values()
print(product_values)

product_items = product_prices.items()
print(product_items)

print('apples' in product_prices)

look_for = 'apples' in product_prices
print(look_for)

