def is_even(num: int) -> bool:
    """Return whether or not the number given is even"""
    return num % 2 == 0

def remove_duplicates(l: list) -> list:
    """Return the given list without duplicates"""
    return list(set(l))