# encoding: utf-8
import operator

# Stock keeping units
SKU = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}


def get_special_offers(items): 
    """
    Update global special offers data horrible hack needs to be refactored once
    working
    """
    group_value = get_group_value(items, 3)
    group_savings = get_group_savings(items, 3)

    return [
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
        },
        {
            'target': 'H',
            'num': 5,
            'type': 'discount',
            'value': 45,
            'saving': 5
        },
        {
            'target': 'H',
            'num': 10,
            'type': 'discount',
            'value': 80,
            'saving': 20
        },
        {
            'target': 'K',
            'num': 2,
            'type': 'discount',
            'value': 150,
            'saving': 10
        },
        {
            'target': 'N',
            'num': 3,
            'type': 'free',
            'value': 'M',
            'saving': SKU['M']
        },
        {
            'target': 'P',
            'num': 5,
            'type': 'discount',
            'value': 200,
            'saving': 50
        },
        {
            'target': 'Q',
            'num': 3,
            'type': 'discount',
            'value': 80,
            'saving': 10
        },
        {
            'target': 'R',
            'num': 3,
            'type': 'free',
            'value': 'Q',
            'saving': SKU['Q']
        },
        {
            'target': 'U',
            'num': 3,
            'type': 'free',
            'value': 'U',
            'saving': SKU['U']
        },
        {
            'target': 'V',
            'num': 2,
            'type': 'discount',
            'value': 90,
            'saving': 10
        },
        {
            'target': 'V',
            'num': 3,
            'type': 'discount',
            'value': 130,
            'saving': 20
        },
        {
            'target': 'S',
            'num': 3,
            'type': 'group_discount',
            'value': group_value,
            'saving': group_savings
        },
        {
            'target': 'T',
            'num': 3,
            'type': 'group_discount',
            'value': group_value,
            'saving': group_savings
        },
        {
            'target': 'X',
            'num': 3,
            'type': 'group_discount',
            'value': group_value,
            'saving': group_savings
        },
        {
            'target': 'Y',
            'num': 3,
            'type': 'group_discount',
            'value': group_value,
            'saving': group_savings
        },
        {
            'target': 'Z',
            'num': 3,
            'type': 'group_discount',
            'value': group_value,
            'saving': group_savings
        }
    ]


def update_special_offers(items, offers): 
    group_value = get_group_value(items, 3)
    group_savings = get_group_savings(items, 3)

    for offer in offers:
        if offer['type'] == 'group_discount':
            offer['value'] = group_value
            offer['saving'] = group_savings
    
    return offers


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


def _get_most_valuable_group_items(items, num):
    group_item_keys = ['S', 'T', 'X', 'Y', 'Z']
    group_items = []
    for item in [x for x in group_item_keys if x in group_item_keys]:
        for x in range(items[item]):
            group_items.append((item, SKU[item]))

    return sorted(group_items, key=lambda x:x[1], reverse=True)[:num]


def get_group_value(items, num):
    group_items = _get_most_valuable_group_items(items, num)
    return sum([x[1] for x in group_items])


def get_group_savings(items, num):
    val = get_group_value(items, num)
    return val - 45 if val > 0 else 0


def get_group_discount(items, item, offer):
    amount = 0
    group_items = _get_most_valuable_group_items(items, 3)

    if len(group_items) == 3:
        amount += 45
        for item in group_items:
            items[item[0]] -= 1

    return amount


def discount_offer(items, item, offer):
    """
    Add discounted items value and remove them once added
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
    def get_required_offer_items(item, offer):
        """
        If the deal is on the same item we need one more item in the 
        basket for it to be valid
        """
        required = offer['num'] 
        if free_item_key == item:
            required += 1
        return required
    
    amount = 0

    if items[item] >= offer['num']:
        free_item_key = offer['value']
        required_items = get_required_offer_items(item, offer)
        free_items = items[item] / required_items
        # Remove free items from items dict
        if items[free_item_key] > 0:
            reduce_by = min(items[free_item_key], free_items)
            items[free_item_key] -= reduce_by
    
    return amount


def calculate_special_offers(items, total):
    """
    Add special offers to total and remove items in offers
    """
    def sort_offers(items, offers):
        return sorted(offers, key=lambda x: x['saving'], reverse=True)
    
    def apply_offer(items, item, offer):
        amount = 0
        item = offer['target']
        if offer.get('type', '') == 'discount':
            amount += discount_offer(items, item, offer)
        if offer.get('type', '') == 'free':
            amount += get_free_offer(items, item, offer)
        if offer.get('type', '') == 'group_discount':
            amount += get_group_discount(items, item, offer)
        return amount
    
    # Get offers largest to smallest savings and apply them
    offers = sort_offers(items, get_special_offers(items))
    while offers:
        offer = offers[0]
        item = offer['target']
        amount = apply_offer(items, item, offer)
        # Keep applying best offer until it cannot be applied any more
        while amount:
            total += amount
            amount = apply_offer(items, item, offer)
        offers.pop(0)
        # Recalculate offers to update group offers
        offers = sort_offers(items, update_special_offers(items, offers))
    
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
    # Create empty dict of all SKU values
    items = {
        key: 0 for key in SKU.keys()
    }

    # Calculate skus found
    for char in skus:
        items[char] += 1
        
    total = calculate_special_offers(items, total)
    
    # Add remaining items
    for item in items:
        total += items[item] * SKU[item]
    
    return total

