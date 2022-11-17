from menu import products
from management import get_product_by_id, get_product_by_type, menu_report, add_product, calculate_tab

if __name__ == "__main__":
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }

    table_1 = [
        {"_id": 1, "amount": 5}, 
        {"_id": 19, "amount": 5}
    ]

    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(get_product_by_id(28))
    print(get_product_by_type('drink'))
    print(menu_report())

    print(add_product(products, **new_product))

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))
    ...
