def get_longest_length(str_list: list[str]):
    """Get string with the longest length from list."""
    if not str_list:
        return None
    return max([str for str in str_list if str is not None], key=len)


def get_first_value(lists: list):
    for value in lists:
        if value:
            return value
    return None


def compare_list(list_1: list[str], list_2: list[str]) -> list:
    """Compare 2 list and return items in list_1 that are present in list_2."""
    if list_1 is None:
        return []
    return [item.strip() for item in list_1 if item.strip().lower() in list_2]


def remove_duplicates_in_list(lists: list):
    combined_list = []
    for lst in lists:
        if lst not in combined_list:
            combined_list.append(lst)

    return combined_list
