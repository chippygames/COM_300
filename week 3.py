
def calculate_discounted_price(price, discount_percent):
    total = (price/20) * discount_percent

    return price - total

print(calculate_discounted_price(100, 0.2))
