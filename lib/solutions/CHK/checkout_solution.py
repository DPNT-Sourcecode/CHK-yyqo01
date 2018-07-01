
# Stock keeping units
SKU = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

SPECIAL_OFFERS = {
    'A': {
        'num': 3,
        'amount': 130
    },
    'B': {
        'num': 2,
        'amount': 45
    }
}


def valid_input(chars):
    """
    Check input is of type string and limited to characters:
    A B C D
    """
    if not isinstance(chars, str):
        return False
    
    for c in chars:
        if c not in ['A', 'B', 'C', 'D']:
            return False

    return False


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not valid_input:
        return -1
    
    items = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }

    # Calculate skus found
    for char in skus:
        items[char] += 1
    
    total = 0

    # Add special offers to total and remove items in offers
    for item in SPECIAL_OFFERS:
        if items[item] > SPECIAL_OFFERS[item]['num']:
            offer_count = items[item] / SPECIAL_OFFERS[item]['num']
            items[item] = items[item] % SPECIAL_OFFERS[item]['num']
            total = offer_count * SPECIAL_OFFERS['amount']
    
    for item in items:
        total += items[item] * SKU[item]
    
    return total

