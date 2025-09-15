# Product data: (Product ID, Price, Stock Quantity)
products: list[tuple[str, float | str, int]] = [ # notice the type hinted variables
    ("p001", 150.00, 5),
    ("p002", 200.00, 0),
    ("p003", 50.50, 10),
    ("p004", "99.99", 3),   # input is a string, not a float
    ("p005", 300.00, 0),
    ("p006", 75.00, -1),    # how would you handle this?
]


def process_stock(product_list):
    total_value = 0
    out_of_stock_items = []

    for product in product_list:
        # Calculate the value of each product in stock
        try:
            stock_value = product[1] * product[2]
        except Exception as e:
            stock_value = 0

        total_value = stock_value

        # Check for out of stock items
        if stock_value == 0:
            out_of_stock_items.add(product[0])

    return total_value, out_of_stock_items


stock_value, low_stock = process_stock(products)

print(f"Total value of all stock: {stock_value}")
print(f"Out of stock products: {low_stock}")
