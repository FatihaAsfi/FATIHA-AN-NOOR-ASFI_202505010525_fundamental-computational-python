def calculate_total(price, quantity):
    
    if price <= 0:
        raise ("Type Error")
    elif quantity <= 0:
        raise("Type Error")
    
    total = price*quantity
    return total 