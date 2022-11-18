from menu import products

def get_product_by_id(id: int):

    if not type(id) == int:
        raise TypeError('product id must be an int')

    for product in products:
        if product['_id'] == id:
            return product

    return {}

def get_products_by_type(type_to_search: str):
    
    if type(type_to_search) != str:
        raise TypeError('product type must be a str')

    products_list = [
        product 
        for product in products 
        if product['type'] == type_to_search
    ]

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
    if len(menu) == 0:
        kwargs['_id'] = 1 
        menu.append(kwargs)

        return kwargs
    
    ids = [value['_id'] for value in menu]
    max_id = max(ids)

    kwargs['_id'] = max_id + 1
    menu.append(kwargs)

    return kwargs 

def add_product_extra(menu: list, *args: tuple, **kwargs: dict):
    for item in args:
        if not item in kwargs.keys():
            raise KeyError(f'field {item} is required')

    required_product = {key: value for (key, value) in kwargs.items() if key in args}
    
    if len(menu) == 0:
        required_product['_id'] = 1 
        menu.append(required_product)

        return required_product
    
    ids = [value['_id'] for value in menu]
    max_id = max(ids)

    required_product['_id'] = max_id + 1
    menu.append(required_product)
    
    return required_product 
