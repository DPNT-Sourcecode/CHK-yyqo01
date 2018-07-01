# encoding: utf-8

# Stock keeping units
SKU = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10
}

SPECIAL_OFFERS = [
    {
        'target': 'A',
        'num': 3,
        'type': 'discount',
        'value': 130,
        'saving': 20
    },
    {
        'target': 'A',
        'num': 5,
        'type': 'discount',
        'value': 200,
        'saving': 50
    },
    {
        'target': 'B',
        'num': 2,
        'type': 'discount',
        'value': 45,
        'saving': 15
    },
    {
        'target': 'E',
        'num': 2,
        'type': 'free',
        'value': 'B',
        'saving': SKU['B']
    },
    {
        'target': 'F',
        'num': 2,
        'type': 'free',
        'value': 'F',
        'saving': SKU['F']
    }
]


def valid_input(chars):
    """
    Check input is of type string and limited to characters:
    in the SKU global
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
    Remove items that have been offered as free for another deal
    """
    amount = 0

    if items[item] >= offer['num']:
        free_items = items[item] / offer['num']
        free_item_key = offer['value']
        if items[free_item_key] > 0:
            reduce_by = min(items[free_item_key], free_items)
            items[free_item_key] -= reduce_by
    
    return amount


def calculate_special_offers(items, total):
    """
    Add special offers to total and remove items in offers
    """
    # Get offers largest to smallest and apply them
    for offer in sorted(SPECIAL_OFFERS, key=lambda x: x['saving'], reverse=True):
        item = offer['target']
        if offer.get('type', '') == 'discount':
            total += discount_offer(items, item, offer)
        if offer.get('type', '') == 'free':
            total += get_free_offer(items, item, offer)
    
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
        key: 0 for key in SKU.keys()
    }

    # Calculate skus found
    for char in skus:
        items[char] += 1
        
    total = calculate_special_offers(items, total)
    
    for item in items:
        total += items[item] * SKU[item]
    
    return total

