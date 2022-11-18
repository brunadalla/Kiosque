from menu import products

def calculate_tab(check: list):
    subtotal = 0

    products_ids = []
    products_prices = []

    for product in products:
        products_ids.append(product['_id'])
        products_prices.append(product['price'])

    for item in check:
        item_id = item['_id']
        item_index = products_ids.index(item_id)
        item_price = products_prices[item_index]

        subtotal += item_price * item['amount']

    subtotal = round(subtotal, 2)

    return {'subtotal': f'${str(subtotal)}'}
