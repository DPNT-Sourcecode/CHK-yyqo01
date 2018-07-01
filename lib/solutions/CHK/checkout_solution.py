# encoding: utf-8

# Stock keeping units
SKU = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

SPECIAL_OFFERS = {
    'A': [
        {
            'num': 3,
            'type': 'discount',
            'value': 130
        },
        {
            'num': 5,
            'type': 'discount',
            'value': 200
        }
    ],
    'B': [
        {
            'num': 2,
            'type': 'discount',
            'value': 45
        }
    ],
    'E': [
        {
            'num': 2,
            'type': 'BOGOF',
            'value': 'E'
        }
    ]
}


def valid_input(chars):
    """
    Check input is of type string and limited to characters:
    A B C D
    """
    if not isinstance(chars, basestring):
        return False
    
    for ch in chars:
        if ch not in ['A', 'B', 'C', 'D']:
            return False

    return True


def calculate_special_offers(items, total):
     # Add special offers to total and remove items in offers
    for item in SPECIAL_OFFERS:
        if items[item] >= SPECIAL_OFFERS[item]['num']:
            offer_count = items[item] / SPECIAL_OFFERS[item]['num']
            items[item] = items[item] % SPECIAL_OFFERS[item]['num']
            total += offer_count * SPECIAL_OFFERS[item]['amount']
    
    return total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Calculate total value of Stock Keeping Units for string of characters
    representing units

    @param skus: (String) string of letters must be of value 'ABCD'
    """
    if not valid_input(skus):
        return -1
    
    total = 0
    items = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }

    # Calculate skus found
    for char in skus:
        items[char] += 1
        
    total = calculate_special_offers(items, total)
    
    for item in items:
        total += items[item] * SKU[item]
    
    return total

