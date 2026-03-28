def validate_side(side):
    if side.upper() not in ["BUY","SELL"]:
        raise ValueError("Invalid side")
    return side.upper()

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET","LIMIT"]:
        raise ValueError("Invalid type")
    return order_type.upper()

def validate_quantity(qty):
    return float(qty)

def validate_price(price):
    return float(price)