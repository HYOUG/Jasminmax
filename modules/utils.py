def is_legal(state: str) -> bool:
    """Check the validity of the state"""
    move_list = [move for move in state]
    for num in range(7):
        if move_list.count(str(num)) > 6:
            return False
    return True


def remove_duplicates(l: list) -> list:
    """Return the given list without duplicates"""
    output = []
    for item in l:
        if item not in output:
            output.append(item)
    return output