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
            'type': 'free',
            'value': 'E'
        }
    ]
}


def valid_input(chars):
    """
    Check input is of type string and limited to characters:
    A B C D E
    """
    if not isinstance(chars, basestring):
        return False
    
    for ch in chars:
        if ch not in SKU.keys():
            return False

    return True


def discount_offer(items, item, offer):
    """
    Add discounted items and remove them once added
    """
    amount = 0

    if items[item] >= offer['num']:
        offer_count = items[item] / offer['num']
        items[item] = items[item] % offer['num']
        amount = offer_count * offer['value']
    
    return amount


def get_free_offer(items, item, offer):
    """
    Add free item this doesn't do anything as we only want the 
    total which the free item doesn't effect
    """
    pass

    # Normally I'd remove this but for this challenge I'll comment it out
    # as I feel I'll need it
    # if items[item] >= offer['num']:
    #     free_item = items[item] / offer['num']
    #     items[free_item] += 1


def calculate_special_offers(items, total):
    """
    Add special offers to total and remove items in offers
    """
    for item in SPECIAL_OFFERS:
        # Get offers largest to smallest and apply them
        for offer in sorted(SPECIAL_OFFERS[item], key=lambda x: x['num'], reverse=True):
            if offer.get('type', '') == 'discount':
                total += discount_offer(items, item, offer)
            if offer.get('type', '') == 'free':
                get_free_offer(items, item, offer)
    
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

