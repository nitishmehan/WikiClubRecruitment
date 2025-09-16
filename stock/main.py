Product = tuple[str, float | str, int]

def process_stock(product_list: list[Product]) -> tuple[float, set[str]]:
    """
    Process a list of products and compute stock statistics.

    Returns:
        Tuple[float, Set[str]]:
            - Total value of all products in stock.
            - Set of product IDs that are out of stock or invalid.
    """
    total_value: float = 0.0
    out_of_stock_items: set[str] = set()

    for pid, price, stock in product_list:
        try:
            numeric_price = float(price)  # Convert price to float
        except (TypeError, ValueError):
            numeric_price = 0.0
            out_of_stock_items.add(pid)  # Mark invalid price as out of stock

        if not isinstance(stock, int) or stock < 0:
            stock = 0  # Normalize invalid stock

        total_value += numeric_price * stock  # Add to total stock value

        if stock == 0:
            out_of_stock_items.add(pid)  # Add out-of-stock items

    return total_value, out_of_stock_items
