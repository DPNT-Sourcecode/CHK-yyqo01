
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
    raise NotImplementedError()
