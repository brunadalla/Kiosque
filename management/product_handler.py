from menu import products

def get_product_by_id(id: int):

    for product in products:
        if product['_id'] == id:
            return product

    return {}

def get_product_by_type(type: str):
    products_list = []

    for product in products:
        if product['type'] == type:
            products_list.append(product)

    return products_list

def menu_report():
    product_count = len(products)
    most_common_type = ''

    types = []
    prices = []
    type_number_of_apperances = 0

    for product in products:
        prices.append(product['price'])
        types.append(product['type'])

    average_price = round(sum(prices) / product_count, 2)
    
    for type in types:
        current_type_apperances = types.count(type)
        if current_type_apperances > type_number_of_apperances:
            type_number_of_apperances = current_type_apperances
            most_common_type = type

    return f'Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}'

def add_product(menu: list, **kwargs: dict):
    new_product = kwargs.copy()
    ids = []

    if len(menu) == 0:
        new_product['_id'] = 1 
        return new_product
    
    for product in menu:
        ids.append(product['_id'])

    max_id = max(ids)

    new_product['_id'] = max_id + 1
    return new_product 
